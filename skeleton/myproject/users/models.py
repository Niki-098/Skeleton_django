from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None, **extra_fields):
        return self.create_user(email, name, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=128, null=False)
    last_login = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=255, unique=True, null=False)
    email = models.EmailField(unique=True, null=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
