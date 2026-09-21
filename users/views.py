from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomAuthenticationForm, ProfileUpdateForm
from django.views.generic import UpdateView

class ProfileEditView(LoginRequiredMixin, UpdateView):
    template_name = 'users/profile_edit.html'
    form_class = ProfileUpdateForm
    model = User
    success_url = reverse_lazy('home')  # Используем reverse_lazy для динамического URL

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Профиль успешно обновлён!')
        return super().form_valid(form)

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = CustomAuthenticationForm

def register(request):
    if request.user.is_authenticated:
        messages.info(request, 'Вы уже авторизованы.')
        return redirect('catalog:home')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Отправка приветственного письма
            send_mail(
                'Добро пожаловать!',
                f'Здравствуйте, {user.email}! Спасибо за регистрацию.',
                'noreply@yoursite.com',
                [user.email],
                fail_silently=False,
            )

            login(request, user)
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('catalog:home')  # выберите один редирект и используйте его везде
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})