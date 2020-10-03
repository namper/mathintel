from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from versatileimagefield.fields import PPOIField, VersatileImageField

from resume.utils import SoftDeletionModel


class Country(SoftDeletionModel):
    name = models.CharField(max_length=255)
    interest_point = PPOIField()
    flag = VersatileImageField(
        _('Flag'),
        upload_to='countries/flags/',
        ppoi_field='interest_point',
    )


class LegacyUser(SoftDeletionModel):
    """ Model To Define Legacy Scientist e.g Newton, Weierstrass, Gödel ... """
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    country = models.ForeignKey(
        to='Country', related_name='legacy_users',
        on_delete=models.PROTECT, null=True, blank=True
    )


class User(AbstractUser):
    country = models.ForeignKey(
        to='Country', related_name='users',
        on_delete=models.PROTECT, null=True, blank=True
    )
