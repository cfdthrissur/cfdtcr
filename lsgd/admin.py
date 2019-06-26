from __future__ import unicode_literals

from django.contrib import admin
from lsgd.models import District, Lsgd, Taluk, Block, Assembly, Parliament

# Register your models here.
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('district_code', 'district_name')

class LsgdAdmin(admin.ModelAdmin):
    list_display = ('lsgd_code', 'lsgd_name', 'lsgd_type','lsgd_taluk', 'lsgd_block')

class TalukAdmin(admin.ModelAdmin):
    list_display = ('taluk_code', 'taluk_name', 'district_code')

class BlockAdmin(admin.ModelAdmin):
    list_display = ('block_code', 'block_name', 'district_code')

class AssemblyAdmin(admin.ModelAdmin):
    list_display = ('assembly_code', 'assembly_name', 'district_code')

class ParliamentAdmin(admin.ModelAdmin):
    list_display = ('parliament_code', 'parliament_name', 'district_code')


admin.site.register(District, DistrictAdmin)
admin.site.register(Lsgd, LsgdAdmin)
admin.site.register(Taluk, TalukAdmin)
admin.site.register(Block, BlockAdmin)
admin.site.register(Assembly, AssemblyAdmin)
admin.site.register(Parliament, ParliamentAdmin)
