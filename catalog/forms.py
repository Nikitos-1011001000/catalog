from django.shortcuts import render, redirect
import os
from django.core.exceptions import ValidationError
from django import forms
from .models import Product

FORBIDDEN_WORDS = [
    'казино', 'криптовалюта', 'крипта', 'биржа',
    'дешево', 'бесплатно', 'обман', 'полиция', 'радар',
]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

            # Placeholder'ы для каждого поля
        placeholders = {
            'name': 'Название товара',
            'description': 'Описание товара',
            'price': '0.00',
            'category': 'Категория',
            'image': 'Выберите изображение',
        }

        for field_name, field in self.fields.items():
                # Bootstrap-класс для всех полей
            field.widget.attrs['class'] = 'form-control'

                # Placeholder
            field.widget.attrs['placeholder'] = placeholders.get(field_name, '')

                # Для textarea — высота
            if isinstance(field.widget, forms.Textarea):
                    field.widget.attrs['rows'] = 4

                # Автофокус на первое поле
            if field_name == 'name':
                field.widget.attrs['autofocus'] = True

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # Проверка формата по расширению
            ext = os.path.splitext(image.name)[1].lower()
            valid_extensions = ['.jpg', '.jpeg', '.png']
            if ext not in valid_extensions:
                raise ValidationError('Допустимые форматы: JPEG, PNG.')

            # Проверка размера (5 МБ = 5 242 880 байт)
            limit = 5 * 1024 * 1024
            if image.size > limit:
                raise ValidationError('Размер файла не должен превышать 5 МБ.')
        return image

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise forms.ValidationError("Цена должна быть больше 0")
        return price

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name.strip()) < 3:
            raise forms.ValidationError("Название должно содержать минимум 3 символа")
        return name

    def clean(self):  # ← вот этого метода не хватает
        cleaned_data = super().clean()
        name = cleaned_data.get('name', '').lower()
        description = cleaned_data.get('description', '').lower()

        text = f"{name} {description}"

        for word in FORBIDDEN_WORDS:
            if word in text:
                field = 'name' if word in name else 'description'
                self.add_error(field, f'Слово "{word}" использовать нельзя.')

        return cleaned_data

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Имя')
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')