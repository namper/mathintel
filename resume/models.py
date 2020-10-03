from django.core.exceptions import ValidationError
from django.db import models
from resume.utils import SoftDeletionModel
from django.utils.translation import gettext_lazy as _
from resume.enum import SCIENCE
from ckeditor_uploader.fields import RichTextUploadingField


class Journal(SoftDeletionModel):
    title = models.CharField(max_length=255)


class Paper(SoftDeletionModel):
    journal = models.ForeignKey(to='Journal', on_delete=models.PROTECT)
    resume = models.ForeignKey(to='Resume', related_name='papers', on_delete=models.PROTECT)

    users = models.ManyToManyField(to='user.User', related_name='papers')
    legacy_users = models.ManyToManyField(to='user.LegacyUser', related_name='papers')

    @property
    def authors(self):
        return self.users.all() or self.legacy_users.all()

    def clean(self):
        # Allow Only Legacy Or Registered User
        if self.users.exists() and self.legacy_users.exists():
            raise ValidationError(_('Authors Can Only Be Legacy Or Registered User'))

    attachment = models.FileField(upload_to='papers')
    publish_date = models.DateField(auto_now=True)


class University(SoftDeletionModel):
    title = models.CharField(max_length=255)
    country = models.ForeignKey(to='user.Country', on_delete=models.CASCADE)


class Field(SoftDeletionModel):
    title = models.CharField(max_length=255)
    science = models.CharField(max_length=2, choices=SCIENCE.choices, default=SCIENCE.GENERAL)
    resume = models.ForeignKey('Resume', related_name='resumes', on_delete=models.PROTECT)

    users = models.ManyToManyField(to='user.User', related_name='fields')
    legacy_users = models.ManyToManyField(to='user.LegacyUser', related_name='fields')


class Resume(SoftDeletionModel):
    publisher = models.ForeignKey(to='user.User', related_name='published_resumes', on_delete=models.CASCADE)
    description = RichTextUploadingField()
