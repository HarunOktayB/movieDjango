from os import error
from django.shortcuts import render
from django.contrib.auth import authenticate
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        authenticate(request, username=username, password=password)

        if(user is not None):
            login(request, user)
            return render(request, 'movies/movies.html')
        else:
            return render(request, 'account/login.html'),{
                "error": "Kullanıcı adı veya şifre hatalı"
            }

def register(request):
    return render(request, 'account/register.html')

def logout(request):
    return render(request, 'movies/movies.html')

def profile(request):
    return render(request, 'account/profile.html')
