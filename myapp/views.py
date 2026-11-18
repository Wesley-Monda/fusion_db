from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import Product
from myapp.my_forms import ProductForm


# Create your views here.
@login_required
def home(request):
    # print('home')

    products = Product.objects.all()  # SELECT * FROM products

    # for product in products:
    #     print(
    #        product.name,
    #        product.code,
    #        product.price,
    #        product.cost,
    #        product.discount
    #      )

    return render(request, 'home.html', {'products': products})

@login_required
def add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'{form.name} has been added successfully')
            return redirect('home')
    else:
        form = ProductForm()
    # Product.objects.get_or_create(
    #     name='Unga',
    #     code=10111101,
    #     price=250.00,
    #     cost=200.00,
    #     category='Food',
    #     for_sale=False
    # )
    #
    # Product.objects.get_or_create(
    #     name='Sugar',
    #     code=10111102,
    #     price=180.00,
    #     cost=150.00,
    #     category='Food',
    #     for_sale=True
    # )
    #
    # Product.objects.get_or_create(
    #     name='Bread',
    #     code=10111103,
    #     price=70.00,
    #     cost=50.00,
    #     category='Food',
    #     for_sale=True
    # )
    #
    # Product.objects.get_or_create(
    #     name='Milk',
    #     code=10111104,
    #     price=120.00,
    #     cost=90.00,
    #     category='Dairy',
    #     for_sale=True
    # )
    #
    # Product.objects.get_or_create(
    #     name='Soap',
    #     code=10111105,
    #     price=80.00,
    #     cost=60.00,
    #     category='Cleaning',
    #     for_sale=True
    # )

    return render(request, 'add.html', {'form': form})

@login_required
def delete_product(request, id):
    product = Product.objects.get(id=id)  # Select * From products Where id=67
    product.delete()
    messages.warning(request, f'{product.name} has been deleted permanently')
    return redirect('home')

@login_required
def edit_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'{product.name} has been updated ')
            return redirect('home')
            return redirect('home')
    else:
        form = ProductForm(instance=product)
    return render(request, "edit.html", {'form': form})

@login_required
def details(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'details.html', {'product': product})

# Group (permissions)
def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'You are now logged in as {user}')
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def signup(request):
    return None

@login_required
def signout(request):
    if request.method == 'POST':
        login(request)
    return redirect('login')