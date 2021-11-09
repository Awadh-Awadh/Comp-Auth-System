from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class CustomBaseUser(BaseUserManager):
    def create_user(self, email, user_name, first_name, password, **others_fields):

      if not email:
          raise ValueError(_("Value must be set"))

      """normalize_email() is used for lowercasing the domain part of """

      email = self.normalize_email(email)
      user = self.model(email=email, user_name=user_name, first_name=first_name, **others_fields)
      user.set_password(password)
      user.save()
      return user




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

     USERNAME_FIELD = 'email'
     REQUIRED_FIELDS = ['user_name']

     def __str__(self):
         return self.user_name
     
     