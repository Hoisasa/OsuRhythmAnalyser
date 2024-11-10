from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register_view, name='AuthRegister'),
    path('logout/', views.logout_view, name='Logout'),
]
