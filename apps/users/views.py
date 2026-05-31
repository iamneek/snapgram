from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model, authenticate, login, logout

User = get_user_model()

def register(request):
    if request.method == 'POST':
        if User.objects.filter(username=request.POST['username']).exists():
            return render(request, 'users/register.html', {'error': 'Username already exists'})
        if User.objects.filter(email=request.POST['email']).exists():
            return render(request, 'users/register.html', {'error': 'Email already exists'})
        if request.POST['password'] != request.POST['confirm_password']:
            return render(request, 'users/register.html', {'error': 'Passwords do not match'})
        try:
            user = User.objects.create_user(username=request.POST['username'], first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
        except IntegrityError:
            return render(request, 'users/register.html', {'error': 'An error occurred while creating the user'})
        login(request, user)
        return redirect('home')
    return render(request, 'users/register.html')