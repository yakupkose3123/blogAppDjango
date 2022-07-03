from django.urls import path
from .views import user_login, user_logout, user_profile, user_register
from .forms import PasswordResetEmailCheck
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('logout/',user_logout,name='logout'),
    path('register/',user_register,name='register'),
    path('login/',user_login,name='login'),
    path('profile/',user_profile,name='profile'),
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name="users/password_reset_email.html", form_class=PasswordResetEmailCheck), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name="password_reset_complete"),
    
]