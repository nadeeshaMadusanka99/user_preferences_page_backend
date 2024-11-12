from django.urls import path
from . import views

#URL config
urlPatterns = [
    path('hello/', views.say_hello)
]
