from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from paintings.models import Painting


# Define the 'cart_contents' function to calculate cart details
def cart_contents(request):
    cart_items = request.session.get('cart', [])
    total = Decimal('0.00')
    total_without_discount = Decimal('0.00')
    clearance_discount = Decimal('0.20')  # 20% discount for clearance items

    # Iterate through each item in the cart
    for item in cart_items:
        painting = get_object_or_404(Painting, id=item['id'])
        frame_price = Decimal(item['frame_price'])
        base_price = Decimal(item['base_price'])

        if painting.subcategory.filter(name='clearance').exists():
            discounted_price = base_price - (base_price * clearance_discount)
            # Use discounted price for clearance items
            total_without_discount += discounted_price + frame_price
        else:
            discounted_price = base_price
            # Use base price for regular items
            total_without_discount += base_price + frame_price

        total += discounted_price + frame_price

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = Decimal('0.00')
        free_delivery_delta = Decimal('0.00')

    # Apply the discount for buying 3-5 paintings
    if len(cart_items) >= 3:
        total -= Decimal('50.00')
        total = max(total, Decimal('0.00'))

    # Apply the discount for buying 6 or more paintings
    if len(cart_items) >= 6:
        total -= Decimal('50.00')
        total = max(total, Decimal('0.00'))

    grand_total = total + delivery

    context = {
        'cart_items': cart_items,
        'total': total.quantize(Decimal('0.00')),
        'delivery': delivery.quantize(Decimal('0.00')),
        'free_delivery_delta': free_delivery_delta.quantize(Decimal('0.00')),
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total.quantize(Decimal('0.00')),
        'total_without_discount':
        total_without_discount.quantize(Decimal('0.00')),
    }

    return context
