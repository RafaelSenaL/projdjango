#views

from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product
from .forms import ProductForm

def index(request):
    lista_produtos = Product.objects.all()
    contexto = {
        'produtos': lista_produtos,
    }
    return render(request, 'vendas/index.html', contexto)

def contacts(request):
    return render(request, 'vendas/contacts.html')

@login_required
def new(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.autor = request.user 
            product.save() 
            
            messages.success(request, 'Produto adicionado com sucesso')
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'vendas/new.html', {'form': form})

def details(request, id):
    p = get_object_or_404(Product, id=id)
    return render(request, 'vendas/details.html', {'product': p})

@login_required
def edit(request, id):
    p = get_object_or_404(Product, id=id)

    if not (request.user.is_staff or p.autor == request.user):
        raise PermissionDenied

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
            messages.success(request, 'produto editado com sucesso')
            return redirect('details', id=id) 
    else:
        form = ProductForm(instance=p)
   
    return render(request, 'vendas/edit.html', {'form': form, 'product': p})

@login_required
def delete(request, id):
    p = get_object_or_404(Product, id=id)

    if not (request.user.is_staff or p.autor == request.user):
        raise PermissionDenied

    if request.method == 'POST':
        p.delete()
        messages.success(request, 'produto apagado com sucesso')
        return redirect('index')
    return render(request, 'vendas/delete.html', {'product': p})