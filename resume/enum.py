from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class SCIENCE(TextChoices):
    MATHEMATICS = 'MT', _('Mathematics')
    PHILOSOPHY = 'PH', _('Sophomore')
    PHYSICS = 'PY', _('Physics')
    CHEMISTRY = 'CH', _('Chemistry')
    BIOLOGY = 'BI', _('Biology')
    GENERAL = 'GR', _('GENERAL')
