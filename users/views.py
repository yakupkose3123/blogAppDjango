from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm #login için 
from .forms import UserForm, UserProfileForm





#!LOGIN
def login(request):
    form = AuthenticationForm(request, data=request.POST) 

    if form.is_valid():
        user = form.get_user() 

        if user:
            messages.success(request,'login successfull')
            login(request, user)
            return redirect('list')

    return render(request, 'users/login.html', {"form":form}) 



def logout(request):
    return render(request, "users/logout.html")
def profile(request):
    return render(request, "users/profile.html")
def register(request):
    return render(request, "users/register.html")