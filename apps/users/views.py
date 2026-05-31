from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model, authenticate, login, logout

User = get_user_model()


def register_view(request):
    if request.method == "POST":
        if User.objects.filter(username=request.POST.get("username")).exists():
            return render(
                request, "users/register.html", {"error": "Username already exists"}
            )
        if User.objects.filter(email=request.POST.get("email")).exists():
            return render(
                request, "users/register.html", {"error": "Email already exists"}
            )
        if request.POST.get("password") != request.POST.get("confirm_password"):
            return render(
                request, "users/register.html", {"error": "Passwords do not match"}
            )
        try:
            user = User.objects.create_user(
                username=request.POST.get("username"),
                first_name=request.POST.get("first_name"),
                last_name=request.POST.get("last_name"),
                email=request.POST.get("email"),
                password=request.POST.get("password"),
            )
        except IntegrityError:
            return render(
                request,
                "users/register.html",
                {"error": "An error occurred while creating the user"},
            )
        login(request, user)
        return redirect("login")
    return render(request, "users/register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        if email:
            try:
                username = User.objects.get(email__exact=email).username
            except User.DoesNotExist:
                return render(
                    request, "users/login.html", {"error": "Account not found!!"}
                )
        user = authenticate(request, username=username, password=password)
        if not user:
            return render(
                request, "users/login.html", {"error": "Invalid Login Details!!"}
            )
        login(request, user)
        return redirect("register")
    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")
