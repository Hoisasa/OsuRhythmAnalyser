from django.urls import path
from . import views

urlpatterns = [
    path('', views.musicStorage, name='MusicCollection'),
    path('photos/', views.photosStorage, name='PhotoCollection'),
]
