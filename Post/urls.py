from .views import PostListApiView,PostSingleAPiView,YoutobeListApiView,YoutobeSingleAPiView
from django.urls import path
# from django.urls import re_path
# from django.http import HttpResponsePermanentRedirect

# def http_to_https(request):
#     if not request.is_secure():
#         # Agar so'rov HTTP bo'lsa, uni HTTPS ga o'zgartiramiz
#         new_url = request.build_absolute_uri().replace('http://', 'https://', 1)
#         return HttpResponsePermanentRedirect(new_url)
#     else:
#         # HTTPS-da davom etish
#         return None

urlpatterns = [
    # re_path(r'^.*$', http_to_https),
  path('',PostListApiView.as_view())   ,
  path('<int:pk>/',PostSingleAPiView.as_view()),
  path('yvideo/',YoutobeListApiView.as_view())   ,
  path('yvideo/<int:pk>/',YoutobeSingleAPiView.as_view()),
]

