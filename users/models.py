from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.

class OKUser(AbstractBaseUser):
    email = models.EmailField(verbose_name= 'Email address', unique= True, max_length= 255)
    username = models.CharField(max_length=255, blank=True, null=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default= True)
    is_blocked = models.BooleanField(default= False)
    date_created = models.DateTimeField(auto_now_add= True)
    date_modified = models.DateTimeField(auto_now = True)

    # create serializer and add auth token

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']