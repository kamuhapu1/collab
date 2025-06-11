from django.shortcuts import render, redirect
from .forms import TableBookingForm
from django.contrib import messages

def main_page(request):
    if request.method == 'POST':
        form = TableBookingForm(request.POST)
        if form.is_valid():
            form.save()
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