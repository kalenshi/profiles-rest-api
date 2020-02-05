from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,
                            PermissionsMixin, BaseUserManager
                            )


class UserProfilesManager(BaseUserManager):

    def create_user(self, email,first_name,last_name, password=None):
        if not email:
            raise ValueError('All Users should provide email')
        email = self.normalize_email(email)
        user = self.model(
        email=email,
        first_name=first_name,
        last_name=last_name
        )
        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email=email,password=password,**extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class UserProfile(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfilesManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return self.first_name + '\t' + self.last_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email
