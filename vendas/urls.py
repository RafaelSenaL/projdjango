#urls vendas

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contacts, name='contatos'),
    path('new/', views.new, name='new'),
    path('product/<int:id>/', views.details, name='detalhe'),
    path('product/<int:id>/edit/', views.edit, name='editar'),
    path('product/<int:id>/delete/', views.delete, name='deletar'),
]