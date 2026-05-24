from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,  # добавьте эту строку
)
from django.views.generic.edit import FormView
from .forms import ProductForm, ContactForm
from .models import Product
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(TemplateView):
    template_name = 'catalog/home.html'


class ContactsView(FormView):
    template_name = 'catalog/contacts.html'
    form_class = ContactForm
    success_url = reverse_lazy('contacts')

    def form_valid(self, form):
        messages.success(self.request, 'Спасибо! Сообщение отправлено.')
        return super().form_valid(form)


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    paginate_by = 10


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    login_url = '/login/'  # URL страницы входа
    redirect_field_name = 'home'
    success_url = reverse_lazy('product_list')

class AddFormsView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/add_forms.html'  # укажите ваш шаблон
    login_url = 'users:login'  # URL страницы входа
    redirect_field_name = 'next'  # параметр для перенаправления после входа
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        # Добавляем сообщение об успешном добавлении товара
        messages.success(self.request, 'Товар успешно добавлен!')
        return super().form_valid(form)

    def form_invalid(self, form):
        # Можно добавить обработку ошибок
        messages.error(self.request, 'Ошибка при добавлении товара. Проверьте данные.')
        return self.render_to_response(self.get_context_data(form=form))

class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'  # URL для перенаправления
    redirect_field_name = 'next'

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'