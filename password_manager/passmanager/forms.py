from django import forms
from django.forms import ModelForm, TextInput, EmailInput


# class LoginForm(forms.Form):
#     user_name = forms.CharField(label="User name", max_length=100, required=True)
#     password = forms.CharField(max_length=32, widget=forms.PasswordInput, required=True)
    

class LoginForm(forms.Form):
    class Meta:
        fields = ['user', 'password']
        widgets = {
            'user': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'User name'
                }),
            'password': forms.PasswordInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Password'
                })
        }