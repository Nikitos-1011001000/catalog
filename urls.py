from django.contrib import admin
from django.urls import path, include  # добавлен include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', include('catalog.urls')),
]
