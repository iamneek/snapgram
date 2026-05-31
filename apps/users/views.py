from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages

User = get_user_model()


def register_view(request):
    
    # TODO: NULL HANDLING / EMPTY VALUES HANDLING
    
    if request.method == "POST":        
        if User.objects.filter(username=request.POST.get("username")).exists():
            messages.error(request, "Username already exists")
            return redirect("register")
        if User.objects.filter(email=request.POST.get("email")).exists():
            messages.error(request, "Email already exists")
            return redirect("register")
        if request.POST.get("password") != request.POST.get("confirm_password"):
            messages.error(request, "Passwords do not match")            
            return redirect("register")
        try:
            user = User.objects.create_user(
                username=request.POST.get("username"),
                first_name=request.POST.get("first_name"),
                last_name=request.POST.get("last_name"),
                email=request.POST.get("email"),
                password=request.POST.get("password"),
            )
        except IntegrityError:
            messages.error(request, "An error occurred while creating the user")            
            return redirect("register")
        login(request, user)
        return redirect("login")
    return render(request, "users/register.html")


def login_view(request):
    

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        if not password or (not username and not email):
            messages.error(request, "Do not leave required fields empty!!")
            return redirect("login")
        if email:
            try:
                username = User.objects.get(email__exact=email).username
            except User.DoesNotExist:
                messages.error(request, "Account not found!!")            
                return redirect("login")
        user = authenticate(request, username=username, password=password)
        if not user:
            messages.error(request, "Invalid Login Details!!")            
            return redirect("login")
        login(request, user)
        return redirect("register")
    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")
