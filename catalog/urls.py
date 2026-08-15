from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('product/new/', views.ProductCreateView.as_view(), name='create_product'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]