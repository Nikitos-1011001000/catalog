from django.shortcuts import render
from django.contrib import messages

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