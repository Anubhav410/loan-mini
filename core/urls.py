from django.contrib import admin
from django.urls import path, include

from core.controllers.auth.api import AuthAPIView

urlpatterns = [
    path('auth/signup', AuthAPIView.sign_up),
    path('auth/login', AuthAPIView.login),
]
