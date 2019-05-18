from django.contrib import admin
from django.urls import path

from sendemail.views import emailView, successView

urlpatterns = [
    path('email/', emailView, name='email'),
    path('success/', successView, name='success'),
]