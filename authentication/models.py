from django.db import models

from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

class OverwriteStorage(FileSystemStorage):
    '''
    Source : https://stackoverflow.com/questions/9522759/imagefield-overwrite-image-file-with-same-name
    '''
    def get_available_name(self, name, max_length=None):
        """Returns a filename that's free on the target storage system, and
        available for new content to be written to.

        Found at http://djangosnippets.org/snippets/976/

        This file storage solves overwrite on upload problem. Another
        proposed solution was to override the save method on the model
        like so (from https://code.djangoproject.com/ticket/11663):

        def save(self, *args, **kwargs):
            try:
                this = MyModelName.objects.get(id=self.id)
                if this.MyImageFieldName != self.MyImageFieldName:
                    this.MyImageFieldName.delete()
            except: pass
            super(MyModelName, self).save(*args, **kwargs)
        """
        # If the filename already exists, remove it as if it was a true file system
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name

# Create your models here.
class UserAccount(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    # address = models.CharField(max_length=50)
    photo = models.ImageField(null=True, blank=True, default="user_picture/default.png",upload_to="user_picture/", storage=OverwriteStorage())
    
    def __str__(self):
        return f"{self.email} | {self.name}"