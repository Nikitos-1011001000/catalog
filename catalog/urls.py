from django.contrib import admin
from django.urls import path, include
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    HomeView,
    ContactsView,
    add_forms  # импортируем функцию
)

app_name = 'catalog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    # Новый маршрут для add_forms:
    path('add/', add_forms, name='add_forms'),  # теперь он здесь
]