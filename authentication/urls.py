from rest_framework import views
from authentication.views import *
from django.urls import path

app_name = 'authentication'

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='user_register'),
    path('login/', LoginAPIView.as_view(), name='user_login'),
    path('user/', AuthUserAPIView.as_view(), name='auth_user'),
]
