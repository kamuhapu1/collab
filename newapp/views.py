from django.shortcuts import render, redirect
from .forms import TableBookingForm, RegisterForm
from django.contrib import messages
from django.contrib.auth import login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm



def main_page(request):
    if request.method == 'POST':
        form = TableBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, "Столик успешно забронирован!")
            return redirect('main_page')
    else:
        form = TableBookingForm()
    return render(request, 'index.html', {'form': form})


def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def menu(request):
    return render(request, 'menu.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно! Вы вошли в аккаунт.')
            return redirect('main_page')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, template_name='user_login.html', context={'form':form})

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def logout(request):
    auth_logout(request)
    messages.success(request, 'Вы вышли из аккаунта.')
    return redirect('main_page')

