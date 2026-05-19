from django.shortcuts import render
from django.contrib import messages
from django.views.generic import DetailView
from django.views.generic import ListView
from .models import Product

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