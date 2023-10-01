import uuid

from django.db import models
from django.db.models import Sum
from decimal import Decimal
from django.conf import settings

from django_countries.fields import CountryField

from paintings.models import Painting
from profiles.models import UserProfile


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    discount_applied = models.BooleanField(default=False)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs and frame prices.
        """

        line_items_count = self.lineitems.count()

        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0

        # Calculate delivery cost based on order total and free
        # delivery threshold
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            delivery_percentage = settings.STANDARD_DELIVERY_PERCENTAGE / 100
            self.delivery_cost = self.order_total * delivery_percentage
        else:
            self.delivery_cost = 0

        # Apply discounts based on the number of line items
        if line_items_count >= 6:
            self.order_total -= Decimal('100.00')
            self.discount_applied = True
        elif line_items_count >= 3:
            self.order_total -= Decimal('50.00')
            self.discount_applied = True
        else:
            self.discount_applied = False

        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order, null=False, blank=False, on_delete=models.CASCADE,
        related_name='lineitems')
    painting = models.ForeignKey(
        Painting, null=False, blank=False, on_delete=models.CASCADE)
    frame = models.CharField(
        # Add a field for frame selection
        max_length=20, null=True, blank=True)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=False, blank=False, editable=False)

    # Add frame choices for selection in admin OrderLineItem model
    FRAME_CHOICES = [
        ('no_frame', 'No Frame'),
        ('standard_frame', 'Standard Frame'),
        ('premium_frame', 'Premium Frame'),
    ]

    frame = models.CharField(
        max_length=20,
        choices=FRAME_CHOICES,
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        base_price = self.painting.price
        frame_price = Decimal('0.00')  # Default frame price as Decimal

        # Calculate the frame price based on the selected frame
        if self.frame == 'standard_frame':
            frame_price = Decimal('50.00')
        elif self.frame == 'premium_frame':
            frame_price = Decimal('100.00')

        # Calculate the discounted price for clearance items
        if self.painting.subcategory.filter(name='clearance').exists():
            # 20% discount for clearance items
            clearance_discount = Decimal('0.20')
            discounted_price = base_price - (base_price * clearance_discount)
        else:
            discounted_price = base_price

        total_price = discounted_price + frame_price

        # Set line item total directly without quantity
        self.lineitem_total = total_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.painting.sku} on order {self.order.order_number}'
