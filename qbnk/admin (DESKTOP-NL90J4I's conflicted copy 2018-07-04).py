from __future__ import unicode_literals

from django.contrib import admin
from qbnk.models import QuestionBank, QuestionHeader

# Register your models here.
class QuestionBankAdmin(admin.ModelAdmin):
   list_display = ('question_code', 'question_text','question_text_m', 'question_type','question_options')

class QuestionHeaderAdmin(admin.ModelAdmin):
    list_display = ('header_code', 'header_text', 'header_text_m','header_remarks')

admin.site.register(QuestionBank, QuestionBankAdmin)
admin.site.register(QuestionHeader, QuestionHeaderAdmin)