from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('contact/', views.contact, name='contact'),
]
