from django.urls import path, include
# Using the default authentication framework
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # previous url
    # path('login/', views.user_login, name='login'), # 127.0.0.1:8000/login/
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout', auth_views.LogoutView.as_view(), name='logout'),
    

    # # password change
    # path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # # confirm password change
    # path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # # Resetting password
    # path('password-reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    # path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    # path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    # path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    # # Dashboard view
    # path('', views.dashboard, name='dashboard'),


    # using the default django authentications
    path('', include('django.contrib.auth.urls'))

]