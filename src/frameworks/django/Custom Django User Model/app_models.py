import uuid

from django.db import models
from django.utils.text import Truncator
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from django.conf import settings



UPLOAD_DIRECTORY_PROFILEPHOTO = 'images_profilephoto'

class CustomUserManager(BaseUserManager):
    """
    Custom user manager to handle all the operations for the Custom User model
    """
    def create_user(self, user_id, mobile_number, email, password, **extra_fields):

        user = self.model(user_id=user_id, mobile_number=mobile_number, email=email, *extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, mobile_number, email, password, **extra_fields):
        user = self.create_user(user_id, mobile_number, email, password, **extra_fields)
        user.is_admin=True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        return self.get(user_id=username)

class User(AbstractBaseUser, PermissionsMixin):
    """
    User that is capable of using the Information System
    """
    GENDER = [
        ('MALE', "MALE"),
        ('FEMALE', "FEMALE"),
        ('TRANSGENDER', "TRANSGENDER"),
        ('PREFER_NOT_TO_SAY', "PREFER_NOT_TO_SAY")
    ]

    user_id = models.CharField(max_length=24, null=True, blank=True, unique=True, help_text="User's unique user id, keep it irrelated with respect to your name or email.")
    full_name = models.CharField(max_length=255, null=True, blank=True, help_text="User's full name")
    gender = models.CharField(max_length=255, choices=GENDER, null=True, blank=True, help_text="User's Gender")
    email = models.EmailField(max_length=255, blank=True, null=True, default='', help_text="User's Email")
    mobile_number = models.CharField(max_length=10, blank=True, null=True, help_text="User's Mobile number")
    profile_photo = models.ImageField(max_length=255, blank=True, null=True, upload_to=UPLOAD_DIRECTORY_PROFILEPHOTO, help_text="User's Profile photo")
    pincode = models.CharField(max_length=6, help_text="User's Residential pincode")

    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['mobile_number', 'email',]
    UNIQUE_TOGETHER = ['user_id', 'email']

    def __str__(self):
        return '%s - %s'%(self.id, self.full_name)

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin