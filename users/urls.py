from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('profile/edit/', views.ProfileEditView.as_view(), name='profile_edit'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]