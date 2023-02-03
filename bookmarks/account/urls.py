from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'), # 127.0.0.1:8000/login/
]