from django.contrib import messages
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ProductForm, ContactForm
from .models import Product

class AddFormsView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/add_forms.html'
    login_url = 'users:login'
    redirect_field_name = 'next'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        messages.success(self.request, 'Товар успешно добавлен!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка при добавлении товара. Проверьте данные.')
        return self.render_to_response(self.get_context_data(form=form))

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
    success_url = reverse_lazy('catalog:product_list')
    login_url = '/accounts/login/'
    redirect_field_name = 'next'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, 'Товар успешно добавлен!')
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')
    login_url = '/accounts/login/'
    redirect_field_name = 'next'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner != request.user:
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Товар успешно обновлён!')
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')
    login_url = '/accounts/login/'
    redirect_field_name = 'next'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner == request.user or request.user.has_perm('catalog.delete_product'):
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseForbidden()