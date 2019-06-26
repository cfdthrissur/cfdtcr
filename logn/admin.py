from __future__ import unicode_literals

from django.contrib import admin
from logn.models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_lsgd','user_type','user_office_phone','user_mobile')

admin.site.register(Profile, ProfileAdmin)
