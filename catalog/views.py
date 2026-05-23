from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, ListView, TemplateView
from django.views.generic.edit import FormView
from .forms import ProductForm, ContactForm
from .models import Product
from django.shortcuts import render


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


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('product_list')

def add_forms(request):
    """Форма для добавления нового товара"""
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog:product_list')  # перенаправление на список товаров
    else:
        form = ProductForm()

    context = {
        'form': form,
    }
    return render(request, 'catalog/add_forms.html', context)