from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from decimal import Decimal
from .forms import OrderForm
from .models import Order, OrderLineItem
from paintings.models import Painting
from cart.contexts import cart_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe_cart_item = request.session.get('stripe_cart_item', [])

        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(stripe_cart_item),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        print(e)
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', [])

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item in cart:
                try:
                    painting_id = item['id']
                    painting = Painting.objects.get(id=painting_id)
                    frame = item['frame']

                    order_line_item = OrderLineItem(
                        order=order,
                        painting=painting,
                        frame=frame,
                    )
                    order_line_item.save()
                except Painting.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        cart = request.session.get('cart', [])
        if not cart:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('paintings'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    for item in order.lineitems.all():
        base_price = item.painting.price
        frame_price = Decimal('0.00')  # Default frame price as Decimal

        if item.frame == 'standard_frame':
            frame_price = Decimal('50.00')
        elif item.frame == 'premium_frame':
            frame_price = Decimal('100.00')

        if item.painting.subcategory.filter(name='clearance').exists():
            clearance_discount = Decimal('0.20')  # 20% discount for clearance items
            discounted_price = base_price - (base_price * clearance_discount)
            item.is_clearance = True
        else:
            discounted_price = base_price
            item.is_clearance = False

        # print(f"Item ID: {item.id}, is_clearance: {item.is_clearance}")

        total_price = discounted_price + frame_price
        item.frame_price = frame_price

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
