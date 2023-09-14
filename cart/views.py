from django.shortcuts import render, redirect, get_object_or_404
from paintings.models import Painting
from decimal import Decimal


def view_cart(request):
    """ A view that renders the cart contents page """
    return render(request, 'cart/cart.html')


def add_to_cart(request):
    sku = request.POST.get('sku')
    frame_price = Decimal('0.00')  # Default frame price as Decimal

    if request.method == 'POST':
        frame = request.POST.get('frame')

        # Find the painting with the matching SKU
        painting = get_object_or_404(Painting, sku=sku)

        # Adjust the frame price based on the user's selection
        if frame == 'standard_frame':
            frame_price = Decimal('10.00')
        elif frame == 'premium_frame':
            frame_price = Decimal('20.00')

        # Calculate the total price including the frame and convert to float
        total_price = float(painting.price + frame_price)

        # Add the painting to the cart with frame information
        cart_item = {
            'sku': painting.sku,
            'name': painting.name,
            'frame': frame,
            'price': total_price,
        }

        # Add the cart item to the session or update if it already exists
        cart = request.session.get('cart', [])
        existing_item = next((item for item in cart if item['sku'] == painting.sku), None)

        if existing_item:
            existing_item.update(cart_item)
        else:
            cart.append(cart_item)

        request.session['cart'] = cart

    return redirect('view_cart')
