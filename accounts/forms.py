from .models import CustomUser, Profile
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class CustomCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email','username','first_name')

class CustomUserChange(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email','username','first_name')
