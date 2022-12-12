from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Post(models.Model):
    post_type = models.CharField(max_length=100)
    post_caption = models.CharField(max_length=200, blank=True)
    post_body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  str(self.created) + ' | ' + self.post_type


class Article(models.Model):
    title = models.CharField(max_length=150)
    title_tag = models.CharField(max_length=100)
    brand_title_tag_postfix = models.BooleanField()
    meta_description = models.CharField(max_length=255)
    featured_image = models.CharField(max_length=200)
    noindex = models.BooleanField()
    body = RichTextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title




