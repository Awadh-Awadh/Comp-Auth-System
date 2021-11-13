from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from random import choice

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, first_name, password, **others_fields):

      if not email:
          raise ValueError(_("Value must be set"))

      """normalize_email() is used for lowercasing the domain part of """

      email = self.normalize_email(email)
      user = self.model(email=email, username=username, first_name=first_name, **others_fields)
      user.set_password(password)
      user.save()
      return user
    def create_superuser(self, email, username, first_name, password, **other_fields):
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

        return self.create_user(email, username, first_name, password, **other_fields)



class CustomUser(AbstractBaseUser, PermissionsMixin):

     """
     gettext is used when data is translated by the endhost
     """

     email = models.EmailField(_('email address'), unique= True)
     username = models.CharField(max_length=200, unique=True)
     first_name = models.CharField(max_length=200)
     start_date = models.DateTimeField(default= timezone.now)
     about = models.CharField(_("about"), max_length=500, blank = True)
     is_staff = models.BooleanField(default= False)
     is_active = models.BooleanField(default = True)
     objects = CustomUserManager()

     USERNAME_FIELD = 'email'
     REQUIRED_FIELDS = ['username', 'first_name']

     def __str__(self):
         return self.username
     
     
class Profile(models.Model):
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  pp = ...
  


class Code(models.Model):
    number = models.CharField(max_length=5, blank = True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    """
    Just before saving the the number we create a random string for it by overiding the save method
    
    
    """


    def save(self, *args, **kwargs):
        """A function that creates five random numbers in a given list of numbers"""
        number_list = [x for x in range(0,11)]
        code_list = []

        for _ in range(5):
            num = choice(number_list)
            code_list.append(num)

        #joining all the five random numbers into a string using a tuple comprehension
        code_string = "".join(str(item) for item in code_list)
        self.number = code_string
        super().save(*args, **kwargs)