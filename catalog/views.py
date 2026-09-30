from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
    PermissionRequiredMixin,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.views import View
from django.views.generic import ListView, FormView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ContactForm, ProductForm
from .models import Category, Product
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .services import (
    clear_products_list_cache,
    get_products_by_category,
    get_products_from_cache,
)

class HomeView(ListView):
    """Главная — список товаров с пагинацией."""
    model = Product
    template_name = 'catalog/home.html'
    paginate_by = 6
    # page_obj попадает в контекст автоматически — шаблон работает без изменений

    def get_queryset(self):
        return get_products_from_cache()

class ContactsView(FormView):
    """Страница контактов — форма обратной связи."""
    template_name = 'catalog/contacts.html'
    form_class = ContactForm
    success_url = reverse_lazy('catalog:contacts')  # поправь на 'catalog:contacts' если нужно

    def form_valid(self, form):
        messages.success(self.request, "Сообщение отправлено!")
        return super().form_valid(form)

@method_decorator(cache_page(60 * 15), name='dispatch')
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


class ProductCreateView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    CreateView
):
    """Уже CBV — не трогаем."""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')
    success_message = "Товар «%(name)s» успешно добавлен!"

    def form_valid(self, form):
        form.instance.owner = self.request.user

        response = super().form_valid(form)

        clear_products_list_cache()

        return response

class ProductUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    SuccessMessageMixin,
    UpdateView
):
    """Обновление товара."""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')
    success_message = "Товар «%(name)s» успешно обновлён!"

    def test_func(self):
        product = self.get_object()

        is_owner = product.owner == self.request.user

        is_moderator = self.request.user.has_perm(
            'catalog.change_product'
        )

        return is_owner or is_moderator

    def form_valid(self, form):
        response = super().form_valid(form)

        clear_products_list_cache()

        return response

class ProductDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    SuccessMessageMixin,
    DeleteView
):
    """Удаление товара."""
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')

    def test_func(self):
        product = self.get_object()

        is_owner = product.owner == self.request.user
        is_moderator = self.request.user.has_perm(
            'catalog.delete_product'
        )

        return is_owner or is_moderator

    def form_valid(self, form):
        response = super().form_valid(form)

        clear_products_list_cache()

        return response

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        name = self.object.name

        messages.success(
            self.request,
            f'Товар «{name}» удалён.'
        )

        response = super().delete(request, *args, **kwargs)

        clear_products_list_cache()

        return response


class ProductUnpublishView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    View
):
    """Отмена публикации доступна только модератору."""
    permission_required = 'catalog.can_unpublish_product'

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        product.is_published = False
        product.save()

        clear_products_list_cache()

        messages.success(
            request,
            f'Публикация товара «{product.name}» отменена.'
        )

        return redirect('catalog:home')

def products_by_category(request, category_id):
    """Страница со всеми товарами выбранной категории."""
    key = f"category_{category_id}"
    category = get_object_or_404(Category, pk=category_id)

    products = get_products_by_category(category_id)

    context = {
        'category': category,
        'products': products,
    }

    return render(
        request,
        'catalog/products_by_category.html',
        context,
        )

