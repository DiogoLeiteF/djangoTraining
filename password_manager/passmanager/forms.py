from django import forms
from django.forms import ModelForm, TextInput, EmailInput



    

class LoginForm(forms.Form):
    # class Meta:
    #     fields = ['user', 'password']
    #     widgets = {
    #         'user': TextInput(attrs={
    #             'class': "form-control",
    #             'style': 'max-width: 300px;',
    #             'placeholder': 'User name'
    #             }),
    #         'password': forms.PasswordInput(attrs={
    #             'class': "form-control", 
    #             'style': 'max-width: 300px;',
    #             'placeholder': 'Password'
    #             })
    #     }
    pass