from django.urls import path
from . import views  # <-- Это работает, потому что views.py лежит в этой же папке catalog

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
]