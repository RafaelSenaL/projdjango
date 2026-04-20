#views

from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def index(request):
    product = Product.objects.all()

    contexto = {
        'product': product,
    }
    return render(request, 'vendas/index.html', contexto)

def contacts(request):
    return render(request, 'vendas/contacts.html')

def new(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'vendas/new.html', {'form': form})