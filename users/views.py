from django.shortcuts import render, redirect, HttpResponse

from django.contrib import messages

from django.contrib.auth import logout, login, authenticate
from .forms import UserForm, UserProfileForm

from django.contrib.auth.forms import AuthenticationForm #login için 


#!REGISTER
def user_register(request):
    form_user = UserForm()
    form_profile = UserProfileForm()

    if request.method == 'POST':
        form_user = UserForm(request.POST) 
        form_profile = UserProfileForm(request.POST, request.FILES) 

        if form_user.is_valid() and form_profile.is_valid():
            user = form_user.save()
            profile = form_profile.save(commit=False) 
            profile.user = user
            profile.save()

            login(request, user) 
            messages.success(request, 'Register Successfull!')

            return redirect('list')

    context = {
        "form_user": form_user,
        "form_profile": form_profile
    }

    return render(request, 'users/register.html',context)



#!LOGIN
def user_login(request):
    form = AuthenticationForm(request, data=request.POST) 

    if form.is_valid():
        user = form.get_user() 

        if user:
            messages.success(request,'login successfull')
            login(request, user)
            return redirect('post_list')

    return render(request, 'users/login.html', {"form":form}) 



def user_logout(request):
    return render(request, "users/logout.html")
def user_profile(request):
    return render(request, "users/profile.html")