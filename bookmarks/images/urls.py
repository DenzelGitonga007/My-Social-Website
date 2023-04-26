from django.urls import path
from . views import image_create

app_name = 'images'

urlpatterns = [
    path('create', views.image_create, name='create'),
]