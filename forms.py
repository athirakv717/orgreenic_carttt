from django import forms
from app1.models import UserRegister
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model=UserRegister
        fields=['first_name','last_name','email','username','password1','password2']



class SignInForm(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20)        

