from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from paintings.models import Painting


def cart_contents(request):
    cart_items = request.session.get('cart', [])
    total = sum(Decimal(item['price']) for item in cart_items)

    total_without_discount = sum(Decimal(item['price']) for item in cart_items)

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    # Apply the discount for buying 3 or more paintings
    if len(cart_items) >= 3:
        total -= Decimal('50.00')
        total = max(total, Decimal('0.00'))

    grand_total = Decimal(total).quantize(Decimal('0.00'))  # Convert back to Decimal

    context = {
        'cart_items': cart_items,
        'total': total,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'total_without_discount': total_without_discount,
    }

    return context
