from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput



class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields=['username','password1','password2']
        widgets = {
            'username': TextInput(attrs={'class':'form-control'}),
        }

class EditProfileForm(UserChangeForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Username'}))
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'First Name'}))
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Last Name'}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'E-mail'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name','last_name','email')