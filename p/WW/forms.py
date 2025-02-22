from django import forms
from django.db import models
from .models import User ,Bill
class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['BillName', 'Duedate', 'Billamount']
