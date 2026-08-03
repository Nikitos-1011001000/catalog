from django.urls import path, include
from . import views
from .views import ProductDetailView, ProductListView, ProductCreateView
from django.contrib import admin

urlpatterns = [

    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('', views.home, name='home'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('contacts/', views.contacts, name='contacts'),
]