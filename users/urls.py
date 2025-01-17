from django.urls import path
from .views import registration, login

urlpatterns = [
    path('registration',registration),
    path('login',login)
]