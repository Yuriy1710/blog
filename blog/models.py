from django.db import models
from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default='Awesome Blog')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.title} {self.author}"
    
    
    