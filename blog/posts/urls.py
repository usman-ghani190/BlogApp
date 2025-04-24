"""Urls for Posts app"""

from django import views
from django.urls import path

from . import views


urlpatterns = [
    path('hello/', views.hello, name='hello' )
]
