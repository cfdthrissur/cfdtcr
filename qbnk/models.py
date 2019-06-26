from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.
class QuestionBank(models.Model):
    question_code = models.CharField(max_length = 10, unique = True, primary_key = True)
    question_text = models.CharField(max_length = 500)
    question_text_m = models.CharField(max_length = 500)
    question_type = models.CharField(max_length = 10)
    question_options = models.CharField(max_length = 200, blank=True)


class QuestionHeader(models.Model):
    header_code = models.CharField(max_length = 10, unique = True, primary_key = True)
    header_text = models.CharField(max_length = 100, unique = True)
    header_text_m = models.CharField(max_length = 100)
    header_remarks = models.CharField(max_length = 200, blank = True)
