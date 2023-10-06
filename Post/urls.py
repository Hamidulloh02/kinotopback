from .views import PostListApiView,PostSingleAPiView
from django.urls import path

urlpatterns = [
 path('',PostListApiView.as_view())   ,
  path('<int:pk>/',PostSingleAPiView.as_view()),
]

