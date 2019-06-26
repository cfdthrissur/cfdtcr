from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    user_lsgd = models.CharField(max_length = 20, blank = True)
    user_type = models.IntegerField(blank = True)
    user_lang = models.IntegerField(blank = True, default = 0)
    user_office_phone = models.CharField(max_length = 25, blank = True, default = "0487 00000000")
    user_mobile = models.CharField(max_length = 25, blank = True, default = "0")


