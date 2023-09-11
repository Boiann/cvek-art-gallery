from django.contrib import admin
from .models import Painting, Category


class PaintingAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'sku',
        'price',
        'size',
        'year',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Painting, PaintingAdmin)
admin.site.register(Category, CategoryAdmin)
