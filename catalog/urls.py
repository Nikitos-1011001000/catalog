from django.urls import path
from .views import HomeView, ContactsView, ProductDetailView, ProductCreateView

app_name = 'catalog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/new/', ProductCreateView.as_view(), name='create_product'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]