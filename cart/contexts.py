from decimal import Decimal
from django.conf import settings


def cart_contents(request):
    cart_items = request.session.get('cart', [])
    total = sum(Decimal(item['price']) for item in cart_items)
    cart = request.session.get('cart', {})

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = Decimal(total).quantize(Decimal('0.00'))  # Convert back to Decimal

    context = {
        'cart_items': cart_items,
        'total': total,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
