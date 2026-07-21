from django.contrib import admin
from django.urls import path, include  # <-- Важно: импортируем include!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')),  #
]