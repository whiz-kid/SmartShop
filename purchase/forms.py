from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['username','email','password']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class UserDetailsForm(forms.Form):
	address = forms.CharField(max_length=2000)
	phone_number = forms.CharField(max_length=20)
