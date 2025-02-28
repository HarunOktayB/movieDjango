from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from .services import UserCreationService

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('movies')  # Ensure this matches the name in movies/urls.py
        else:
            return render(request, 'account/login.html', {"error": "Kullanıcı adı veya şifre hatalı"})

    return render(request, 'account/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        user_type = request.POST.get('user_type')

        try:
            user = UserCreationService.create_user(username, password, email, first_name, user_type)
            user.save()
            return redirect('login')
        except IntegrityError:
            return render(request, 'account/register.html', {"error": "Bu kullanıcı adı zaten kullanılıyor."})

    return render(request, 'account/register.html')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')

@login_required
def profile(request):
    return render(request, 'account/profile.html')
