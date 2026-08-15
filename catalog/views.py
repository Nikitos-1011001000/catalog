from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import ContactForm, ProductForm  # ← добавлен ProductForm
from .models import Product


def home(request):
    products = Product.objects.all().order_by('-created_at')
    paginator = Paginator(products, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'catalog/home.html', {'page_obj': page_obj})


def contacts(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, "Сообщение отправлено!")
            return redirect("contacts")
    else:
        form = ContactForm()

    return render(request, 'catalog/contacts.html', {"form": form})


def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        messages.error(request, "Товар не найден")
        return redirect('home')
    return render(request, 'catalog/product_detail.html', {'product': product})

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('product_list')