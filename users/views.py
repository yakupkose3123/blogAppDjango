from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from .forms import UserUpdateForm, ProfileUpdateForm, RegistrationForm
from django.contrib.auth.forms import AuthenticationForm #login için 


#!REGISTER
def user_register(request):
    form = RegistrationForm(request.POST or None) 
    if request.user.is_authenticated:
        messages.warning(request, "You are already have an account!")
        return redirect("blog:post_list")
    if form.is_valid():
        form.save()
        name = form.cleaned_data["username"]
        messages.success(request, f"Account created for {name}")
        return redirect("users:login")  
                
    context = {
        "form" : form
    }
    return render(request, "users/register.html", context)



#!LOGIN
def user_login(request):
    form = AuthenticationForm(request, data=request.POST) 

    if form.is_valid():
        user = form.get_user() 

        if user:
            messages.success(request,'login successfull')
            login(request, user)
            return redirect('blog:post_list')

    return render(request, 'users/login.html', {"form":form}) 



#!LOGOUT
def user_logout(request):
    messages.success(request, 'You logged out!')
    logout(request)
    
    return render(request, "users/logout.html")

#!PROFİLE
@login_required
def user_profile(request):
    u_form = UserUpdateForm(request.POST or None, instance=request.user)
    p_form = ProfileUpdateForm(request.POST or None, instance=request.user.profile, files=request.FILES)
    
    if u_form.is_valid() and p_form.is_valid():
        u_form.save()
        p_form.save()
        messages.success(request, "Your profile has been updated!")
        return redirect(request.path)
    
    context = {
        "u_form" : u_form,
        "p_form" : p_form    
    }
    return render(request, "users/profile.html", context)

