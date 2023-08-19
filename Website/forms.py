from django import forms
from django.contrib.auth.models import User
from django.core import validators
from Website.models import UserProfileInfo

# class NewUser(forms.ModelForm):
#     # If needed, Add some validation for each field
#     first_name = forms.CharField(validators=[validators.MaxLengthValidator(8)])
#     class Meta:
#         model = User
#         fields = '__all__'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model  = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')