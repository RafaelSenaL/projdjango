#views

from django.shortcuts import render
from .models import Product

def index(request):
    product = Product.objects.all()

    contexto = {
        'product': product,
    }
    

    
    return render(request, 'vendas/index.html', contexto)
def contacts(request):
    return render(request, 'vendas/contacts.html')