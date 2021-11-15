from .models import Code, CustomUser, Profile
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms


class CustomCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email','username','first_name')

class CustomUserChange(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email','username','first_name')

class CodeForm(forms.ModelForm):
    number = forms.CharField(label='Code', help_text= "Please Enter verification code sent to your email")
    class Meta:
        model = Code
        fields = ('number',)
