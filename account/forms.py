from typing import Any
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import AccountUser
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = AccountUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = AccountUser
        fields = ("email",)





class LoginForm(forms.Form):
    username = forms.CharField(required=False, widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "jobwey username"}
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control", "placeholder": "example@website.com"}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "password"}
    ))
    agree_to_terms = forms.CharField(widget=forms.CheckboxInput(attrs={"class": "form-check-input", "id": "flexCheckDefault"}))

    def clean_email(self):
        return self.cleaned_data['email']
    
    def clean_password(self):
        return self.cleaned_data['password']
    
    def clean_username(self):
        return self.cleaned_data['username']
    

        



class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control", "placeholder": "example@website.com"}
    ))

    def clean_email(self):
        return self.cleaned_data['email']
    
    