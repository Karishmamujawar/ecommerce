from django.shortcuts import render,redirect, get_object_or_404
from .models import Product
# Create your views here.

def product_list(request):
    products = Product.objects.all()
   
    return render(request, 'store/product_list.html', {'products': products})

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('cart')

def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    for pid, qty in cart.items():
        product = get_object_or_404(Product, id=pid)
        total += product.price * qty
        cart_items.append({
    'product': product,
    'quantity': qty,
    'subtotal': product.price * qty
})
       
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total': total})

def checkout(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    for pid, qty in cart.items():
        product = get_object_or_404(Product, id=pid)
        total += product.price * qty
        cart_items.append({
    'product': product,
    'quantity': qty,
    'subtotal': product.price * qty
})
        
    return render(request, 'store/checkout.html', {'cart_items': cart_items, 'total': total})


def increase_quantity(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        cart[str(product_id)] += 1
    request.session['cart'] = cart
    return redirect('cart')

def decrease_quantity(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        if cart[str(product_id)] > 1:
            cart[str(product_id)] -= 1
        else:
            del cart[str(product_id)]
    request.session['cart'] = cart
    return redirect('cart')
