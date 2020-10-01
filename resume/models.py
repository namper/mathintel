from django.db import models
from resume.utils import SoftDeletionModel


class Field(SoftDeletionModel):
    resume = models.ForeignKey('Resume', related_name='fields', on_delete=models.PROTECT)


class Resume(SoftDeletionModel):
    owner = models.ForeignKey(to='user.User', null=True, on_delete=models.CASCADE)
