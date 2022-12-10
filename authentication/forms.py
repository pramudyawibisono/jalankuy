from django import forms
from .models import UserAccount

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=50, label="Email", widget=forms.EmailInput(attrs={
            'placeholder' : 'Masukan Email Anda','class':'form-control', 'aria-describedby':'inputGroupPrepend'})
            )
    password = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder' : 'Masukan Password Anda','class':'form-control', 'aria-describedby':'inputGroupPrepend'}), label="Password")

class RegisterForm(forms.ModelForm):
    conf_password = forms.CharField(label="Konfirmasi Password", widget=forms.PasswordInput (
        attrs={'placeholder' : 'Konfirmasi Password Anda','class':'form-control','aria-describedby':'inputGroupPrepend',})
        )
    
    class Meta:
        model = UserAccount
        fields = ["email", "username", "password", "conf_password", "name", "phone"]
        
        labels = {
            "email": "Email",
            "username": "Username",
            "password": "Password",
            "name": "Nama", 
            "phone":"No. Telepon", 
            "photo":"Foto Profil",
        }
        
        widgets = {
            'email' : forms.TextInput(
                attrs={
                'type' : 'email',
                'placeholder' : 'Masukan Email Anda',
                'class':'form-control',
                'aria-describedby':'inputGroupPrepend',
                }
            ),
            'username' : forms.TextInput(
                attrs={
                'type' : 'text',
                'placeholder' : 'Masukan Username Anda',
                'class':'form-control',
                'aria-describedby':'inputGroupPrepend',
                }
            ),
            'password' : forms.TextInput(
                attrs={
                'type' : 'password',
                'placeholder' : 'Masukan Password Anda',
                'class':'form-control',
                'aria-describedby':'inputGroupPrepend',
                }
            ),
            'name' : forms.TextInput(
                attrs={
                'type' : 'text',
                'placeholder' : 'Masukan Nama Anda',
                'class':'form-control',
                'aria-describedby':'inputGroupPrepend',
                }
            ),
            'phone' : forms.TextInput(
                attrs={
                'type' : 'tel',
                'placeholder' : 'Masukan Nomor Telepon Anda',
                'class':'form-control',
                'aria-describedby':'inputGroupPrepend',
                }
            ),
        }
        