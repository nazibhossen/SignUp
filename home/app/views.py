from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error = 'Invalid username or password'
    return render(request, 'login.html')


def registration(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "User arleady exist")
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email arleady exist")
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email
                )
                user.set_password(password1)
                user.save()
                messages.success(request, "Profile successfully created")
                return redirect('login')
    return render(request, 'registration.html')


@login_required
def home(request):
    return render(request, 'index.html')


def logout(request):
    auth.logout(request)
    messages.success(request, 'Log Out Successfully')
    return redirect('login')
