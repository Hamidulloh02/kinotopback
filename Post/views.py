from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import BaseAuthentication
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView
from .models import Post
from .serializers import PostSerializers
import jwt
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from django.conf import settings


class PostListApiView(CreateAPIView,ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class PostSingleAPiView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers


