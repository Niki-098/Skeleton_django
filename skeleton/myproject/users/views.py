from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserLoginForm
from django.utils import timezone



from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Home Page!")

def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            user = authenticate(request, name=name, password=password)
            if user is not None:
                login(request, user)
                user.last_login = timezone.now()
                user.save()
                return redirect('home')  # Redirect to a home page or another page
            else:
                form.add_error(None, "Invalid name or password")
    else:
        form = CustomUserLoginForm()
    return render(request, 'login.html', {'form': form})


from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # or wherever you want to redirect after signup
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('login')

class CustomPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    success_url = '/password_reset/done/'  # Adjust URL as needed


# Create your views here.
