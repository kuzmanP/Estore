from django.urls import path

from .import views



urlpatterns = [
    path('', views.index,   name = 'index'),
    path('Checkout/', views.Checkout,   name = 'Checkout'),
    path('Product/', views.Product,   name = 'Product'),
]