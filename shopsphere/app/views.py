from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from app.models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

# Create your views here.
def home(request):
    return render(request,"ss/home.html")

def register(request):

    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered. Please login with your email.")
            return redirect('register')
        
        if pass1 != pass2:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        myuser = User.objects.create_user(username=email, email=email, password=pass1, first_name=fname, last_name=lname)

        myuser.save()
        messages.success(request,"Registration successfull")
        return redirect('login_page')

    return render(request,"ss/register.html")

def login_page(request):

    if request.method == "POST":
        email = request.POST['email']
        pass1 = request.POST['pass1']

        user = authenticate(username=email, password=pass1)

        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.error(request,"Invalid email or password")
            return redirect('login_page')
    
    return render(request,"ss/login.html")

def signout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login_page')
    
@never_cache
@login_required(login_url='login_page')
def main(request):
    products = Product.objects.all()
    return render(request,"ss/main.html",{'products':products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'ss/product_detail.html', {'product': product})

@login_required  # Only logged-in users can add to cart
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    # Check if product is already in cart for that user
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)

    if not created:
        # Already exists → just increase quantity
        cart_item.quantity += 1
        cart_item.save()

    return redirect('product_detail', product_id=product_id)

@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    discount = (total_price*0.25)
    shipping = 99 if total_price > 999 else 0
    amount_payble = (total_price - discount + shipping)
    # views.py (cart view or wherever amount payable is calculated)
    request.session['amount_payable'] = amount_payble

    return render(request, 'ss/cart.html', {'cart_items': cart_items, 'total_price': total_price, 'discount': discount, 'shipping': shipping, 'amount_payble':amount_payble})

def increase_quantity(request, item_id):
    item = get_object_or_404(Cart, id=item_id, user=request.user)
    item.quantity += 1
    item.save()
    return redirect('cart')

def decrease_quantity(request, item_id):
    item = get_object_or_404(Cart, id=item_id, user=request.user)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()  # optional: remove item if quantity is 1
    return redirect('cart')

def payment_page(request):
    amount_payable = request.session.get('amount_payable', 0)
    return render(request, 'ss/payment.html', {'amount_payable': amount_payable})

from django.shortcuts import render, redirect

def confirm_order(request):
    if request.user.is_authenticated:
        user_name = request.user.last_name or request.user.username
    else:
        user_name = "Guest"

    # Optionally clear cart session or DB entries here

    return render(request, 'ss/success.html', {'user_name': user_name})



