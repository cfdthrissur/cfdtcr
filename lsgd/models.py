from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.
class District(models.Model):
    district_code = models.CharField(max_length = 10, unique = True, primary_key=True)
    district_name = models.CharField(max_length = 50, unique = True)

class Taluk(models.Model):
    taluk_code = models.CharField(max_length = 15, unique = True, primary_key = True)
    district_code = models.ForeignKey('District', on_delete = models.SET_NULL, null = True)
    taluk_name = models.CharField(max_length = 100)

class Block(models.Model):
    block_code = models.CharField(max_length = 15, unique = True, primary_key = True)
    district_code = models.ForeignKey('District', on_delete = models.SET_NULL, null = True)
    block_name = models.CharField(max_length = 100)
    
class Assembly(models.Model):
    assembly_code = models.CharField(max_length = 15, unique = True, primary_key = True)
    assembly_name = models.CharField(max_length = 100)
    district_code = models.ForeignKey('District', on_delete = models.SET_NULL, null = True)


class Parliament(models.Model):
    parliament_code = models.CharField(max_length = 15, unique = True, primary_key = True)
    parliament_name = models.CharField(max_length = 100)
    district_code = models.ForeignKey('District', on_delete = models.SET_NULL, null = True)


class Lsgd(models.Model):
    lsgd_code = models.CharField(max_length = 15, unique = True, primary_key = True)
    lsgd_name = models.CharField(max_length = 100, unique = True)
    lsgd_type = models.CharField(max_length = 15)
    lsgd_district = models.ForeignKey('District', on_delete = models.SET_NULL, null=True)
    lsgd_taluk = models.ForeignKey('Taluk', on_delete = models.SET_NULL, null = True)
    lsgd_block = models.ForeignKey('Block', on_delete = models.SET_NULL, null = True)
    lsgd_assembly = models.ForeignKey('Assembly', on_delete = models.SET_NULL, null = True)
    lsgd_parliament = models.ForeignKey('Parliament', on_delete = models.SET_NULL, null = True)



