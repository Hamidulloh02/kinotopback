import jwt
from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=500)
    link = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __self__(self):
        return self.title
