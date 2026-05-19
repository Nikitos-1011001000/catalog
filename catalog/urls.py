from django.urls import path
from . import views
from .views import ProductDetailView

urlpatterns = [
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]