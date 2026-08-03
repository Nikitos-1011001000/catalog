from django.shortcuts import render
from django.contrib import messages
from django.views.generic import DetailView, CreateView, ListView
from .models import Product, Contact
from .forms import ProductForm, ContactForm
from django.urls import reverse_lazy
from .models import Contact

def home(request):
    latest_products = Product.objects.order_by('-id')[:5]
    print(list(latest_products))
    return render(request, 'catalog/home.html', {
        'latest_products': latest_products
    })

def contacts_page(request):
    contacts = Contact.objects.all()
    print("В базе контактов:", contacts.count())  # ← смотрите в консоль
    for c in contacts:
        print(" -", c.name)
    return render(request, 'catalog/contacts.html', {'contacts': contacts})

def contacts(request):
    contact_data = Contact.objects.first()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Здесь сохраните или отправьте
            messages.success(request, 'Спасибо! Сообщение отправлено.')
            return redirect('contacts')
    else:
        form = ContactForm()

    return render(request, 'catalog/contacts.html', {
        'form': form,
        'contact_data': contact_data,
    })

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    paginate_by = 10

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('product_list')