from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, name, username, password=None):
        if not name:
            raise ValueError("Users must enter a name!")
        if not username:
            raise ValueError("Users must have a valid mobile no.")

        user  = self.model(
                name = name,
                username = username,
			)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, username, password):
        user  = self.create_user(
                username = username,
				name=name,
                password=password
			)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    name                    = models.CharField(verbose_name='name', max_length=100)
    username                = models.CharField(verbose_name = 'phone_no', max_length=30, unique=True)
    # phone                   = models.BigIntegerField(verbose_name='phone_no', unique=True)
    date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin				= models.BooleanField(default=False)
    is_active				= models.BooleanField(default=True)
    is_staff				= models.BooleanField(default=False)
    is_superuser			= models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS= ['name']

    objects = MyAccountManager()
    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True