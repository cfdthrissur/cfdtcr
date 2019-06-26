from __future__ import unicode_literals

from django.contrib import admin
from data.models import D001, D002, D003, D004, D007, D008, D012, D019, D016

# Register your models here.
class D001Admin(admin.ModelAdmin):
    list_display = ('lsgd_code_and_year', 'lsgd_name','lsgd_year_of_formation','lsgd_area_in_sqkm','lsgd_no_of_wards','lsgd_taluk_name','lsgd_block_panchayath_wards')

class D002Admin(admin.ModelAdmin):
    list_display = ('lsgd_code_and_year', 'population_male', 'population_female')

class D003Admin(admin.ModelAdmin):
    list_display = ('lsgd_code_and_year', 'children_male_below_age_1')

class D004Admin(admin.ModelAdmin):
    list_display = ('lsgd_code_and_year', 'Total_disabled_M')

class D007Admin(admin.ModelAdmin):
    list_display = ('lsgd_code_and_year', 'S_7_Live_Birth_G')

class D008Admin(admin.ModelAdmin):
    list_display = ('lsgd_code_and_year', 'Newborn_measured')

class D012Admin(admin.ModelAdmin):
    list_display = ('lsgd_code_and_year', 'No_of_School')

class D019Admin(admin.ModelAdmin):
    list_display = ('lsgd_code_and_year', 'Zero_Zone')

class D016Admin(admin.ModelAdmin):
    list_display = ('lsgd_code_and_year', 'Under_Orphanges')

admin.site.register(D001, D001Admin)
admin.site.register(D002, D002Admin)
admin.site.register(D003, D003Admin)
admin.site.register(D004, D004Admin)
admin.site.register(D007, D007Admin)
admin.site.register(D008, D008Admin)
admin.site.register(D012, D012Admin)
admin.site.register(D019, D019Admin)
admin.site.register(D016, D016Admin)