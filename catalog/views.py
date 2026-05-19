from django.shortcuts import render
from django.contrib import messages
from django.views.generic import DetailView, CreateView, ListView
from .models import Product
from .forms import ProductForm
from django.urls import reverse_lazy

def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    return render(request, 'catalog/contacts.html')

def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Здесь сохраните или отправьте
            messages.success(request, 'Спасибо! Сообщение отправлено.')
            return render(request, 'catalog/contacts.html')
    else:
        form = ContactForm()
    return render(request, 'catalog/contacts.html', {'form': form})

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

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