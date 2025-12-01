# CONF/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'online-courses-html-template/index.html')

def about(request):
    return render(request, 'online-courses-html-template/about.html')

def contact(request):
    return render(request, 'online-courses-html-template/contact.html')

def home(request):
    return render(request, 'index.html')  # home.html emas, sizda index.html bor
