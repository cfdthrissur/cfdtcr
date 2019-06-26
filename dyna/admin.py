from __future__ import unicode_literals

from django.contrib import admin
from dyna.models import Qbank

# Register your models here.
class QbankAdmin(admin.ModelAdmin):
    list_display = ('Qcode', 'Qname','Qtype','Qoptions')

admin.site.register(Qbank, QbankAdmin)