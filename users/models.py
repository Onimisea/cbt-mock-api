from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone
import datetime


class UserManager(BaseUserManager):
    def create_user(self, fullname, jamb_reg_num, password, **extra_fields):
        if not fullname:
            raise ValueError("Participants must have a Firstname and Lastname")

        if not jamb_reg_num:
            raise ValueError("Participants must have a JAMB Registration Number")

        user = self.model(
            fullname=fullname,
            jamb_reg_num=jamb_reg_num,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, fullname, jamb_reg_num, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser should have is_staff set to True")
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser should have is_superuser set to True")

        return self.create_user(fullname=fullname, jamb_reg_num=jamb_reg_num, password=password, **extra_fields)
    

class User(AbstractBaseUser, PermissionsMixin):
    fullname = models.CharField(max_length=100, verbose_name="Firstname Lastname", null=False, blank=False)
    
    jamb_reg_num = models.CharField(max_length=15, verbose_name="JAMB Registration Number", null=False, blank=False, unique=True)
    
    generated_password = models.CharField(max_length=9, verbose_name="Generated Password", null=False, blank=False, unique=False)
    
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "jamb_reg_num"
    EMAIL_FIELD = "jamb_reg_num"
    REQUIRED_FIELDS = ['fullname', 'generated_password']

    objects = UserManager()

    def __str__(self):
        return self.fullname