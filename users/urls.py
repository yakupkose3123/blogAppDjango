from django.urls import path
from .views import user_login, user_logout, user_profile, user_register

urlpatterns = [
    path('logout/',user_logout,name='logout'),
    path('register/',user_register,name='register'),
    path('login/',user_login,name='login'),
    path('profile/',user_profile,name='profile'),
]