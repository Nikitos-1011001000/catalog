from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def home(request):
    # Ищем шаблон строго по пути: catalog/templates/catalog/home.html
    return render(request, 'catalog/home.html', {})


def contacts(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, "Сообщение отправлено!")
            # ВАЖНО: без пробела между redirect и скобками!
            return redirect("contacts")
    else:
        form = ContactForm()

    # ИЩЕМ ШАБЛОН ЗДЕСЬ: catalog/templates/catalog/contacts.html
    return render(request, 'catalog/contacts.html', {"form": form})