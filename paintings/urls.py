from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_paintings, name='paintings'),
    path('<int:painting_id>', views.painting_detail, name='painting_detail'),
    path('add/', views.add_painting, name='add_painting'),
    path('edit/<int:painting_id>/', views.edit_painting, name='edit_painting'),
]
