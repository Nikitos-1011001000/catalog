from django import forms
from .models import Product

BAD_WORDS = [
    'казино',
    'криптовалюта',
    'крипта',
    'биржа',
    'дешево',
    'бесплатно',
    'обман',
    'полиция',
    'радар',
]

ALLOWED_IMAGE_TYPES = ['image/jpeg', 'image/png']
MAX_IMAGE_SIZE = 5 * 1024 * 1024  # 5 MB


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Имя')
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
            })

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        lower_name = name.lower()

        for bad_word in BAD_WORDS:
            if bad_word in lower_name:
                raise forms.ValidationError(
                    'Название не должно содержать запрещённые слова.'
                )

        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        lower_description = description.lower()

        for bad_word in BAD_WORDS:
            if bad_word in lower_description:
                raise forms.ValidationError(
                    'Описание не должно содержать запрещённые слова.'
                )

        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price is not None and price < 0:
            raise forms.ValidationError('Цена не может быть отрицательной.')

        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')

        if image:
            if image.content_type not in ALLOWED_IMAGE_TYPES:
                raise forms.ValidationError('Разрешены только JPEG и PNG изображения.')

            if image.size > MAX_IMAGE_SIZE:
                raise forms.ValidationError('Размер изображения не должен превышать 5 МБ.')

        return image