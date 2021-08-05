from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PremissionMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        '''Create and saves a new User'''
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user