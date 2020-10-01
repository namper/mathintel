from django.db import models


class Field(models.Model):
    resume = models.ForeignKey('Resume', related_name='fields', on_delete=models.PROTECT)


class Resume(models.Model):
    owner = models.ForeignKey(to='user.User', null=True, on_delete=models.CASCADE)
