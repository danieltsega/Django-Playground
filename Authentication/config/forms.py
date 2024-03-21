from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class CustomUserForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'h-10 w-full border rounded focus:outline-none py-3 px-3 text-gray-700  mr-2 bg-slate-200 mb-4',
        'placeholder': 'Enter First Name...'
    }), label='First Name',)
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'h-10 w-full border rounded focus:outline-none py-3 px-3 text-gray-700  mr-2 bg-slate-200 mb-4',
        'placeholder': 'Enter Last Name...'
    }), label='Last Name')
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'h-10 w-full border rounded focus:outline-none py-3 px-3 text-gray-700  mr-2 bg-slate-200 mb-4',
        'placeholder': 'Enter Email...'
    }), label='Email')
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'h-10 w-full border rounded focus:outline-none py-3 px-3 text-gray-700  mr-2 bg-slate-200 mb-4',
        'placeholder': 'Enter UserName...'
    }), label='User Name')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'h-10 w-full border rounded focus:outline-none py-3 px-3 text-gray-700  mr-2 bg-slate-200 mb-4',
        'placeholder': 'Enter Password...'
    }), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'h-10 w-full border rounded focus:outline-none py-3 px-3 text-gray-700  mr-2 bg-slate-200 mb-4',
        'placeholder': 'Confirm Password...'
    }), label='Confirm Password')
    
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class CustomLoginForm(AuthenticationForm):
    
    def get_invalid_login_error(self):
        return forms.ValidationError(
            _("Incorrect username or password."),
            code='invalid_login'
        )
    
    
    """    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'h-10 w-full border rounded focus:outline-none py-3 px-3 text-gray-700  mr-2 bg-slate-200',
        'placeholder': 'Enter Email...'
    }), label='')
    """
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'h-10 w-full border rounded focus:outline-none py-3 px-3 text-gray-700  mr-2 bg-slate-200 mb-4',
        'placeholder': 'Enter UserName...'
    }), label='Username')
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'h-10 w-full border rounded focus:outline-none py-3 px-3 text-gray-700  mr-2 bg-slate-200 mb-4',
        'placeholder': 'Enter Password...'
    }), label='Password')
    
    
    class Meta:
        model = User
        fields = ['username', 'password']
        error_message = ''
