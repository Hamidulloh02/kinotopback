import jwt
from rest_framework import serializers
from .models import Post,Youtobe
from django.conf import settings



class PostSerializers(serializers.ModelSerializer):
        class Meta:
            model = Post
            fields = ('id','title','link','created_at')


class YoutobeSerializers(serializers.ModelSerializer):
        class Meta:
            model = Youtobe
            fields = ('id','title','link','created_at')