from django.contrib import admin
from .models import Painting, Category, SubCategory


# Configure the admin interface for the Painting model
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


# Configure the admin interface for the Category model
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


# Configure the admin interface for the SubCategory model
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


# Register the configured admin classes for each model
admin.site.register(Painting, PaintingAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
