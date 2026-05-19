from django.urls import path
from . import views
from .views import ProductDetailView

urlpatterns = [
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
]