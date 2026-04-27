#urls vendas

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('new/', views.new, name='new'),
    path('product/<int:id>/', views.details, name='details'),
    path('product/<int:id>/edit/', views.edit, name='edit'),
    path('product/<int:id>/delete/', views.delete, name='delete'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('carrinho/adicionar/<int:id>/', views.adicionar_ao_carrinho, name='add_cart'),
    path('remover_carrinho/<int:item_id>/', views.remover_carrinho, name='remover_carrinho'),
    path('cart/', views.cart, name='cart'),
    path('profile/', views.profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)