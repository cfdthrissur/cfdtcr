from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# create your models here.
class Qbank(models.models):
    QCode = models.IntegerField(null = True)
    Qname = models.CharField(max_length = 50)
    QType = models.IntegerField(null = True)
    QOptions = models.CharField(max_length = 50)
    