from .views import PostListApiView
from django.urls import path

urlpatterns = [
 path('',PostListApiView.as_view())   
]

