from django.db import models
from .manager import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class AccessToken(models.Model):
    userid = models.IntegerField()
    jti = models.CharField(max_length=100, unique=True, null=False)


class  Users(AbstractBaseUser, PermissionsMixin):
    username: None
    email = models.CharField(max_length=50, null=False, unique=True)
    fname = models.CharField(max_length=50, null=False)
    bio = models.CharField(max_length=200, null=True)
    link = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=100, default="Male")
    img_src = models.CharField(max_length=100, default="default_user.png")
    modified_by = models.CharField(max_length=50, null=True)
    total_follower = models.IntegerField(default=0)
    total_music = models.IntegerField(default=0)
    total_album = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)
    is_disabled = models.BooleanField(default=False)
    is_artist = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = None
    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELD = []

    # def create_user(self, email, password, **extra_fields):
    #     self.objects.create_user(email=email, password=password, **extra_fields)


    def __str__(self):  
        return self.email



