from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, email, user_name, first_name, password, **others_fields):

      if not email:
          raise ValueError(_("Value must be set"))

      """normalize_email() is used for lowercasing the domain part of """

      email = self.normalize_email(email)
      user = self.model(email=email, user_name=user_name, first_name=first_name, **others_fields)
      user.set_password(password)
      user.save()
      return user
    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active',True)

        if other_fields.get('is_staff') is not True:
          raise ValueError(
            "Super user must be assigned to is_stuff=True"
          )

        if other_fields.get('is_superuser') is not True:
            raise ValueError(
              "Super user must be assigned to is_superuser=True"

            )

        return self.create_user(email, user_name, first_name, password, **other_fields)



class CustomUser(AbstractBaseUser, PermissionsMixin):

     """
     gettext is used when data is translated by the endhost
     """

     email = models.EmailField(_('email address'), unique= True)
     user_name = models.CharField(max_length=200, unique=True)
     first_name = models.CharField(max_length=200)
     start_date = models.DateTimeField(default= timezone.now)
     about = models.CharField(_("about"), max_length=500, blank = True)
     is_staff = models.BooleanField(default= False)
     is_active = models.BooleanField(default = False)
     objects = CustomUserManager()

     USERNAME_FIELD = 'email' or 'user_name'
     REQUIRED_FIELDS = ['user_name', 'first_name']

     def __str__(self):
         return self.user_name
     
     
class Profile(models.Model):
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  pp = ...
  
