#urls vendas

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('new/', views.new, name='new'),
    path('product/<int:id>/', views.details, name='details'),
    path('product/<int:id>/edit/', views.edit, name='edit'),
    path('product/<int:id>/delete/', views.delete, name='delete'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('carrinho/adicionar/<int:id>/', views.adicionar_ao_carrinho, name='add_cart'),
    path('cart/', views.cart, name='cart')
]