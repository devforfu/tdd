from django.db import models
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class ListUserManager(BaseUserManager):

    def create_user(self, email):
        ListUser.objects.create(email=email)

    def create_superuser(self, email, password):
        self.create_user(email)


class ListUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(primary_key=True)
    USERNAME_FIELD = 'email'

    objects = ListUserManager()

    @property
    def is_staff(self):
        return self.email == 'admin@admin.com'

    @property
    def is_active(self):
        return True

    def get_full_name(self):
        return self.email.split('@')[0]

    def get_short_name(self):
        return self.email



