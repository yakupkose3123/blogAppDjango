from django.contrib.auth.models import User
from .models import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
class RegistrationForm(UserCreationForm):
    email = forms.EmailField()  #?override ettik, email artık zorunlu. boş bırakınca default required true oldu
    
    class Meta:
        model = User
        fields = ("username", "email")
       
    def clean_email(self):  #?her emailin unique olmasını istediğimizde custom validation  a tabi tutuyoruz  
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Please use another Email, that one already taken")
        return email
    
    # def clean_first_name(self): #name içinde a varsa kabul etme yoksa kabul et.
    #     name = self.cleaned_data("first_name")
    #     if "a" in name:
    #         raise forms.ValidationError("Your name includes A")
    #     return name
        
class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ("image", "bio")

class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("username", "email")

class PasswordResetEmailCheck(PasswordResetForm): #! Burada amaç password reset yaparken db de olmayan bir e mail girildiğinde ona şifre göndermeyelim diye.    
    def clean_email(self):
        email = self.cleaned_data["email"]
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("There is no email")
        return email