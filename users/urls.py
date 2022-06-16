from django.urls import path
from .views import login, logout, profile, register

urlpatterns = [
    path('logout/',logout,name='logout'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('profile/',profile,name='profile'),
]