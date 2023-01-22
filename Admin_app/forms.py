
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product

class Admin_login_form(UserCreationForm):
    pass


class ProductForm(forms.ModelForm):

  class Meta:
    model=Product
    fields=['name','strap_color','highlights','price','image','status']