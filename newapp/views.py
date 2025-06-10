from django.shortcuts import render

def main_page(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def menu(request):
    return render(request, 'menu.html')