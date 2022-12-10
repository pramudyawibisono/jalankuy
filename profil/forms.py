from django import forms
from authentication.models import UserAccount

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ["name", "phone", "photo"]
        
        labels = {
            "name": "Nama", 
            "phone":"No. Telepon", 
            "photo":"Foto Profil"
        }
        
        widgets = {
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
            'photo' : forms.FileInput(
                attrs={
                "accept":"image/*",
                'placeholder' : 'Masukan profile foto Anda',
                'class':'form-control',
                'aria-describedby':'inputGroupPrepend',
                }
            ),
        }

class EditPasswordForm(forms.ModelForm):
    old_password = forms.CharField(label="Password Lama", widget=forms.PasswordInput(
        attrs={'class':'form-control', 'placeholder':'Masukan password lama'}
        )
    )   
    conf_password = forms.CharField(label="Konfirmasi Password Baru", widget=forms.PasswordInput(
        attrs={'class':'form-control', 'placeholder':'Masukan konfirmasi password baru'}
        )
    )
    class Meta:
        model = UserAccount
        fields = ["old_password","password","conf_password"]
        
        labels = { 
            "password":"Password Baru", 
        }
        
        widgets = {
            'password' : forms.TextInput(
                attrs={
                'type' : 'password',
                'placeholder' : 'Masukan Password Baru Anda',
                'class':'form-control',
                'aria-describedby':'inputGroupPrepend',
                }
            ),
        }
