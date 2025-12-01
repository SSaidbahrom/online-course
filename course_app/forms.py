from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Product, Order, Comment, CustomUser

# Login va Register formalar
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')

# ModelFormlar
class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ()

class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('product',)

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('product',)

# Kontakt formasi
class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Product, Order, Comment, CustomUser

# Login va Register formalar
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')

# ModelFormlar
class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ()

class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('product',)

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('product',)

# Kontakt formasi
class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
