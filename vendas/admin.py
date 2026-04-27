from django.contrib import admin
from .models import Product, Contact

admin.site.register(Product)

@admin.register(Contact)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'assunto', 'data_envio')
    search_fields = ('nome', 'email', 'assunto')
    readonly_fields = ('data_envio',)