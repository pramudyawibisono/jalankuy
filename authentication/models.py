from django.db import models

# Create your models here.
class UserAccount(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    # address = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="static/user_profile_picture")
    
    def __str__(self):
        return f"{self.email} | {self.name}"