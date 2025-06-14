from django.shortcuts import render, redirect
from .forms import TableBookingForm, RegisterForm
from django.contrib import messages
from .models import Post, Comment
from django.contrib.auth import login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404
from .forms import CommentForm
from django.core.paginator import Paginator

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

    latest_posts = Post.objects.all().order_by('-date')[:4]

    context = {
        'form': form,
        'latest_posts': latest_posts,
    }
    return render(request, 'index.html', context)


def blog(request):
    all_posts = Post.objects.all().order_by('-date')
    paginator = Paginator(all_posts, 4)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(request, 'blog.html', {'page_obj': page_obj})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post).order_by('-created_date')

    if request.method == 'POST':
        text = request.POST.get('text', '').strip()
        if not text:
            messages.error(request, "Комментарий не может быть пустым")
        else:
            if request.user.is_authenticated:
                author = request.user.username
            else:
                author = 'Гость'

            Comment.objects.create(
                post=post,
                author=author,
                text=text
            )
            messages.success(request, "Комментарий добавлен!")
            return redirect('post_detail', post_id=post.id)

    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments,
        'request': request
    })

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

