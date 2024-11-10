from django.urls import path
from . import views

app_name = 'DjangoService'

urlpatterns = [
    path('', views.MusicStorage.as_view(), name='MusicCollection'),

]
