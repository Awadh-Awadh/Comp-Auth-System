from django.dispatch import receiver
from .models import CustomUser, Profile, Code
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model



@receiver(post_save, sender = get_user_model())
def create_profile(sender, instance, created, **kwargs):
    if created:
       Profile.objects.create(user = instance)



"""
When a user is created create a code for the user

"""

@receiver(post_save, sender = CustomUser)
def user_generate_code(sender, instance, created, *args, **kwargs):
    if created:
        Code.objects.create(user = instance)
