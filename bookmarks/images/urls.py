# from django.urls import path
# from . import views

# app_name = 'images'

# urlpatterns = [
#     path('create/', views.image_create, name='create'),
# ]


from django.urls import path
from . import views

app_name = 'images'

urlpatterns = [
    path('create/', views.image_create, name='create'),
    path('detail/<int:id>/<slug:slug>/', views.image_detail, name='detail'), # have the image display after saving
    path('like/', views.image_like, name='like'), # like and unlike
    # path('', views.image_list, name='list'),
]