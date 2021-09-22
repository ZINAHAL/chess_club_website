from django import forms
from django.contrib.auth.models import User

#Form to be used for logging users in
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)