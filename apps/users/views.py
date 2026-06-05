from django.db import IntegrityError
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import EditUser, EditProfile
from django.db.models import Q
from django.http import HttpResponse


User = get_user_model()


def register_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not username or not first_name or not last_name or not email or not password:
            messages.error(request, "Do not leave fields empty!!")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect("register")

        if password != request.POST.get("confirm_password"):
            messages.error(request, "Passwords do not match")
            return redirect("register")
        try:
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
            )
        except IntegrityError:
            messages.error(request, "An error occurred while creating the user")
            return redirect("register")
        login(request, user)
        return redirect("feed")
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
        print("login done")
        return redirect("feed")
    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    posts = user.posts.all()
    return render(request, "users/profile.html", {"user": user, "posts": posts})


@login_required
def edit_profile_view(request, username):
    if not request.user.username == username:
        messages.error(request, "Error, you can only edit your own profile...")
        return redirect("profile", username=username)

    user = get_object_or_404(User, username=username)
    profile = user.profile

    if request.method == "POST":
        user_form = EditUser(request.POST, instance=user)
        profile_form = EditProfile(request.POST, request.FILES, instance=profile)

        if not (user_form.is_valid() and profile_form.is_valid()):
            messages.error(
                request, "Error editing profile, please verify your entries..."
            )
            return redirect("profile", username=user.username)

        user_form.save()
        profile_form.save()
        return redirect("profile", username=user.username)

    else:
        user_form = EditUser(instance=user)
        profile_form = EditProfile(instance=profile)
        return render(
            request, "users/edit.html", {"user": user_form, "profile": profile_form}
        )


@login_required
def search_view(request):
    query = request.GET.get('q', '').strip()
    if not query:
        return HttpResponse("")
    users = User.objects.filter(Q(username__icontains=query) | Q(first_name__icontains=query) | Q(last_name__icontains=query)).exclude(id=request.user.id)[:8]
    return render(request, "users/search_results.html", {'user_list': users})