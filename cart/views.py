from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse
from paintings.models import Painting
from decimal import Decimal
from django.contrib import messages


def view_cart(request):
    """ A view that renders the cart contents page """
    return render(request, 'cart/cart.html')


def add_to_cart(request, painting_id):
    id = request.POST.get('id')
    frame_price = Decimal('0.00')  # Default frame price as Decimal
    cart = request.session.get('cart', [])

    clearance_discount = Decimal('0.20')  # 20% discount for clearance items

    if request.method == 'POST':
        frame = request.POST.get('frame')

        # Find the painting with the matching id
        painting = get_object_or_404(Painting, id=id)

        # Set a default frame value if it's not provided in the request
        if not frame:
            frame = 'no_frame'  # You can choose your default frame value

        # Adjust the frame price based on the user's selection
        if frame == 'standard_frame':
            frame_price = Decimal('50.00')
        elif frame == 'premium_frame':
            frame_price = Decimal('100.00')

        subcategory_names = [subcategory.name for subcategory in painting.subcategory.all()]
        base_price = painting.price

        # Calculate the discounted price for clearance items
        if painting.subcategory.filter(name='clearance').exists():
            discounted_price = base_price - (base_price * clearance_discount)
        else:
            discounted_price = base_price

        total_price = discounted_price + frame_price

        if painting.subcategory.filter(name='clearance').exists():
            is_clearance = True
        else:
            is_clearance = False

        # Add the painting to the cart with frame information
        cart_item = {
            'id': painting.id,
            'sku': painting.sku,
            'name': painting.name,
            'frame': frame,
            'price': str(total_price),
            'image_url': painting.image.url,
            'size': painting.size,
            'year': str(painting.year),
            'base_price': str(base_price),
            'frame_price': str(frame_price),
            'subcategory': subcategory_names,
            'undiscounted_price': str(base_price),
            'is_clearance': is_clearance,
        }

        existing_item = next((item for item in cart if item['id'] == painting.id), None)

        if existing_item:
            existing_item.update(cart_item)
        else:
            cart.append(cart_item)
            messages.success(request, f'Added {painting.name} to your cart')

        request.session['cart'] = cart

    return redirect('painting_detail', painting_id=painting_id)


def remove_painting(request, painting_id):

    painting = get_object_or_404(Painting, id=painting_id)

    if request.method == 'POST':
        cart = request.session.get('cart', [])

        # Create a new cart without the item to be removed
        updated_cart = [item for item in cart if item['id'] != painting_id]

        # Update the session with the new cart
        request.session['cart'] = updated_cart
        messages.info(request, f'Removed {painting.name} from your cart!')

    return redirect('view_cart')


def adjust_frame(request, painting_id):

    painting = get_object_or_404(Painting, id=painting_id)

    if request.method == 'POST':
        frame = request.POST.get('frame')
        cart = request.session.get('cart', [])

        for item in cart:
            if item['id'] == painting_id:
                item['frame'] = frame
                # Adjust the frame price based on the selected frame
                if frame == 'no_frame':
                    item['frame_price'] = '0.00'
                elif frame == 'standard_frame':
                    item['frame_price'] = '50.00'
                elif frame == 'premium_frame':
                    item['frame_price'] = '100.00'

                # Recalculate the total price based on the base price and adjusted frame price
                item['price'] = str(Decimal(item['base_price']) + Decimal(item['frame_price']))
                break

        request.session['cart'] = cart
        messages.info(request, f'Updated frame in your cart!')

    return redirect('view_cart')
