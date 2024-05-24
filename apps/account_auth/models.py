from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
  is_super_admin = models.BooleanField("Is Super Admin", default=False)
  is_institution_admin = models.BooleanField("Is Institution Admin", default=False)
  is_institution_user = models.BooleanField("Is Institution User", default=False)