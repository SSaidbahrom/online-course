from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

def contact(request):
    return render(request, 'contact.html')

def contact(request, id=None):  
    return render(request, 'contact.html')

# Home page
def home(request):
    return render(request, 'home.html')

# About page
def about(request):
    return render(request, 'about.html')

# Course page
def course(request):
    return render(request, 'course.html')

# Teacher page
def teacher(request):
    return render(request, 'teacher.html')

# Blog list page
def blog_list(request):
    return render(request, 'blog_list.html')

# Blog detail page
def blog_detail(request, id):
    return render(request, 'blog_detail.html', {'id': id})

# Login
def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user_obj = User.objects.get(email=email)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None

            if user is not None:
                login(request, user)
                return redirect('app:index')
            else:
                messages.error(request, "Email yoki password noto‘g‘ri")
    else:
        form = LoginForm()
    
    return render(request, 'user/login.html', {'form': form})

# Register
def register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            messages.success(request, "Ro'yxatdan muvaffaqiyatli o'tdingiz")
            return redirect('user:login_page')
    else:
        form = RegisterForm()
    
    return render(request, 'user/register.html', {'form': form})

# Logout
def logout_page(request):
    logout(request)
    return redirect('app:index')

def home(request):
    return render(request, 'index.html')  # home.html emas, sizda index.html bor
