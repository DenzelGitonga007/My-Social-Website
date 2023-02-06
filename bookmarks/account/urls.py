from django.urls import path
# Using the default authentication framework
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # previous url
    # path('login/', views.user_login, name='login'), # 127.0.0.1:8000/login/
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    # Dashboard view
    path('', views.dashboard, name='dashboard'),

    # password change
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # confirm password change
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # Resetting password
    
]