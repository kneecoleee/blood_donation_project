from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, CustomUserCreationForm, ProfileForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if hasattr(user, 'profile'):
                    login(request, user)
                    return redirect('homepage')
                else:
                    return redirect('account:profile_create')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('account:profile_create')
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/register.html', {'form': form})

def profile_create_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('homepage')
    else:
        form = ProfileForm()
    return render(request, 'account/profile_create.html', {'form': form})