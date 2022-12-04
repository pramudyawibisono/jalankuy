from django import forms
from .models import UserAccount

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(forms.ModelForm):
    
    class Meta:
        model = UserAccount
        fields = ["email", "username", "password", "name", "phone"]
        