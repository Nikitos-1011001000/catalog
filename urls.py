from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('catalog.urls')),
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls', namespace='catalog')),
]
