from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<int:painting_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_painting/<int:painting_id>/', views.remove_painting, name='remove_painting'),
    path('adjust_frame/<int:painting_id>/', views.adjust_frame, name='adjust_frame'),
]
