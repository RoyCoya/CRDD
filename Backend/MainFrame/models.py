from django.db import models
from django.contrib.auth import settings

class Test(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='记录id')
    comments = models.CharField(null=True, blank=True, max_length=200, verbose_name='备注')
