from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'autofocus': True})
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')

        if username:
            try:
                # Ищем пользователя по email
                user = User.objects.get(email=username)
                cleaned_data['username'] = user.username
            except User.DoesNotExist:
                raise forms.ValidationError('Пользователь с таким email не найден.')
        return cleaned_data

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['avatar', 'phone', 'country']