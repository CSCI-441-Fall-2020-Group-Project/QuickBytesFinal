'''
  // written by: Patrick Carra & Kegan Ronholt
  // tested by: Patrick Carra & Kegan Ronholt
  // debugged by: Patrick Carra & Kegan Ronholt
'''

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


# This controls the registration form
class registerForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    
    class Meta:
        model = User
        fields = ['first_name','last_name', 'username', 'email','password1','password2']
        widget = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.TextInput(attrs={'class': 'form-control'}),
            'password2': forms.TextInput(attrs={'class': 'form-control'}),
        }




