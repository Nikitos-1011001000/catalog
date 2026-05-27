from django.contrib import admin
from django.urls import path, include
from . import views
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    HomeView,
    ContactsView,
    AddFormsView,
    ProductUpdateView,
    ProductDeleteView,
    ProductsByCategoryView,
)

app_name = 'catalog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('add/', views.AddFormsView.as_view(), name='add_forms'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('category/<int:category_id>/', ProductsByCategoryView.as_view(), name='products_by_category'),
]