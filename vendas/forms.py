from django import forms
from .models import Contact, Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['nome', 'marca', 'preço', 'imagem', 'descricao']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['nome', 'email', 'assunto', 'mensagem']