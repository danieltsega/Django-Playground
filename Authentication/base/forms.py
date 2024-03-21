from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomUserForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'h-10 w-full border rounded focus:outline-none py-3 px-3 text-gray-700  mr-2 bg-slate-200',
        'placeholder': 'Enter First Name...'
    }), label='',)
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'h-10 w-full border rounded focus:outline-none py-3 px-3 text-gray-700  mr-2 bg-slate-200',
        'placeholder': 'Enter Last Name...'
    }), label='')
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'h-10 w-full border rounded focus:outline-none py-3 px-3 text-gray-700  mr-2 bg-slate-200',
        'placeholder': 'Enter Email...'
    }), label='')
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'h-10 w-full border rounded focus:outline-none py-3 px-3 text-gray-700  mr-2 bg-slate-200',
        'placeholder': 'Enter UserName...'
    }), label='')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'h-10 w-full border rounded focus:outline-none py-3 px-3 text-gray-700  mr-2 bg-slate-200',
        'placeholder': 'Enter Password...'
    }), label='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'h-10 w-full border rounded focus:outline-none py-3 px-3 text-gray-700  mr-2 bg-slate-200',
        'placeholder': 'Confirm Password...'
    }), label='')
    
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class CustomLoginForm(AuthenticationForm):
    """    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'h-10 w-full border rounded focus:outline-none py-3 px-3 text-gray-700  mr-2 bg-slate-200',
        'placeholder': 'Enter Email...'
    }), label='')
    """
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'h-10 w-full border rounded focus:outline-none py-3 px-3 text-gray-700  mr-2 bg-slate-200',
        'placeholder': 'Enter UserName...'
    }), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'h-10 w-full border rounded focus:outline-none py-3 px-3 text-gray-700  mr-2 bg-slate-200',
        'placeholder': 'Enter Password...'
    }), label='')
    
    
    class Meta:
        model = User
        fields = ['username', 'password']
