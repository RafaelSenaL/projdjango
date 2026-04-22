#views

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
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

@login_required
def new(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'vendas/new.html', {'form': form})

def details(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'vendas/details.html', {'product': product})

@login_required
def edit(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('detalhe', id=id)
    else:
        form = ProductForm(instance=product)
    return render(request, 'vendas/edit.html', {'form': form, 'product': product})

@login_required
def delete(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('index')
    return render(request, 'vendas/delete.html', {'product': product})