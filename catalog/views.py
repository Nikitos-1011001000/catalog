from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.views.generic import ListView, FormView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ContactForm, ProductForm
from .models import Product

class HomeView(ListView):
    """Главная — список товаров с пагинацией."""
    model = Product
    queryset = Product.objects.all().order_by('-created_at')
    template_name = 'catalog/home.html'
    paginate_by = 6
    # page_obj попадает в контекст автоматически — шаблон работает без изменений


class ContactsView(FormView):
    """Страница контактов — форма обратной связи."""
    template_name = 'catalog/contacts.html'
    form_class = ContactForm
    success_url = reverse_lazy('catalog:contacts')  # поправь на 'catalog:contacts' если нужно

    def form_valid(self, form):
        messages.success(self.request, "Сообщение отправлено!")
        return super().form_valid(form)


class ProductDetailView(DetailView):
    """Детальная страница товара с редиректом вместо 404."""
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        queryset = queryset or self.get_queryset()
        try:
            return queryset.get(pk=self.kwargs.get(self.pk_url_kwarg))
        except Product.DoesNotExist:
            messages.error(self.request, "Товар не найден")
            return None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object is None:
            return redirect('catalog:home')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class ProductCreateView(SuccessMessageMixin, CreateView):
    """Уже CBV — не трогаем."""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')
    success_message = "Товар «%(name)s» успешно добавлен!"

class ProductUpdateView(SuccessMessageMixin, UpdateView):
    """Обновление товара."""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')
    success_message = "Товар «%(name)s» успешно обновлён!"


class ProductDeleteView(SuccessMessageMixin, DeleteView):
    """Удаление товара."""
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        name = self.object.name  # ← сохраняем имя ДО удаления
        messages.success(self.request, f'Товар «{name}» удалён.')
        return super().delete(request, *args, **kwargs)

