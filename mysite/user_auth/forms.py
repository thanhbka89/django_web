"""
Cac lop Form
"""

from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(label='Email')

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 100)
    password = forms.CharField(widget = forms.PasswordInput())