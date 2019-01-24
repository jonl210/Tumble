from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm
from .models import Profile

#Sign up new user
def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            new_user = User.objects.create_user(username, email, password)
            Profile.objects.create(user=new_user)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("home")

#Log out user
@login_required
def log_out_user(request):
    logout(request)
    return redirect("home")

#Log in user
def log_in_user(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect("home")
    else:
        return redirect("login_view")

#Display user account
def account(request):
    return render(request, "users/account.html")

#Display all user's bookmarks
def user_bookmarks(request):
    profile = Profile.objects.get(user=request.user)
    bookmarks = profile.bookmarks.all()
    return render(request, "users/bookmarks.html", {"bookmarks": bookmarks})

#Display user's public bookmarks
def user_public_bookmarks(request):
    profile = Profile.objects.get(user=request.user)
    bookmarks = profile.bookmarks.all().filter(public=True)
    return render(request, "users/public_bookmarks.html", {"bookmarks": bookmarks})

#Display user's private bookmarks
def user_private_bookmarks(request):
    profile = Profile.objects.get(user=request.user)
    bookmarks = profile.bookmarks.all().filter(public=False)
    return render(request, "users/private_bookmarks.html", {"bookmarks": bookmarks})
