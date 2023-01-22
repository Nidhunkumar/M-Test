from django.shortcuts import render,redirect
from .models import Account,Address,trial
from django.contrib import messages
from django.contrib.auth import logout
from Admin_app.models import Product
from allauth.socialaccount.models import SocialAccount# step 3 made this possible
# Create your views here.
def UserIndex(request):
  context={}
  products=Product.objects.all()
  context['products']=products

  return render(request,'user_templates/index.html',context)

def UserLogin(request):
  return render(request,'user_templates/login.html')
def UserRegister(request):
  context={}
  if request.method == "POST":
      username    = request.POST['username']
      first_name  = request.POST['first_name']
      last_name   = request.POST['last_name']
      email       = request.POST['email']
      phone_number = request.POST['phone_number']
      password1   = request.POST['password1']
      password2   = request.POST['password2']
      # phone_number    = request.POST['phone_number'] 
      if password1 != password2 :
              messages.error(request,"password not matching", extra_tags='signuppassword')
              return redirect(UserRegister)

             
      if Account.objects.filter(username = username).exists():
          print('GETTING INTO USERNAME')
          messages.error(request, "Username already taken", extra_tags='signupusername')
          return redirect(UserRegister)
      if Account.objects.filter(email = email).exists():
          print('GETTING INTO EMAIL')
          messages.error(request,"Email already taken", extra_tags='signupemail')
          return redirect(UserRegister)
      else:
                    
                    user = Account.objects.create_user(username= username,first_name =first_name ,last_name=last_name,email = email,phone_number=phone_number, password = password1)
                    
                    user.save()
                    return redirect(UserIndex)
  else:
        return render(request,'user_templates/signup.html'  )

def Userlogout(request):
    logout(request)
    return redirect(UserIndex)

from Admin_app.models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')

