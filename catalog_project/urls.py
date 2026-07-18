from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Всё остальное (главную, контакты и т.д.) мы берём из приложения catalog
    path('', include('catalog.urls')),
]
