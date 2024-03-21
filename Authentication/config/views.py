from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserForm, CustomLoginForm
from django.contrib.auth.views import LoginView

class SignUpView(CreateView):
    form_class = CustomUserForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    
class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'registration/login.html'