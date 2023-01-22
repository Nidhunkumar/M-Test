from django.shortcuts import render,redirect
from .forms import Admin_login_form,ProductForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,authenticate
from django.contrib import messages


from .models import Product


# Create your views here.
def Adminlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect(admindashboard)
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request = request,
                    template_name = 'admin_templates/admin_login.html',
                    context={"form":form})

def admindashboard(request):
   context={}
   products=Product.objects.all()
   


   form = ProductForm()
   context = {'form': form,'products':products}
   return render(request,'admin_templates/admin_dashboard.html',context)

def add_product(request):
   print(request.method)
   if request.method == 'POST':
      form=ProductForm(request.POST,request.FILES)
      if form.is_valid():
         form.save()
         Product_name=form.cleaned_data.get('name')
         return redirect(admindashboard)

def UpdateProduct(request,id):
    context={}
    updating_product=Product.objects.get(id=id)
    if request.method=='POST':
        form=ProductForm(request.POST or None,request.FILES or None,instance=updating_product)
        if form.is_valid():
            form.save()
            return redirect(admindashboard)
    else:
        form=ProductForm(instance=updating_product)

    context['form']=form
    return render(request,'admin_templates/update_product.html',context)

    