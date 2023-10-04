import jwt
from rest_framework import serializers
from .models import Post
from django.conf import settings



class PostSerializers(serializers.ModelSerializer):
        class Meta:
            model = Post
            fields = ('id','title','link')