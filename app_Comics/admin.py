from django.contrib import admin
from .models import Producto, Proveedor, Cliente

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre_Empresa', 'nombre_Contacto', 'telefono_Contacto', 'email_Contacto', 'ciudad')
    list_filter = ('ciudad', 'pais')
    search_fields = ('nombre_Empresa', 'nombre_Contacto')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'autor', 'editorial', 'precio', 'stock', 'proveedor')
    list_filter = ('genero', 'editorial', 'tipo_producto')
    search_fields = ('nombre', 'autor', 'isbn')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'ciudad', 'fecha_registro')
    list_filter = ('ciudad', 'pais')
    search_fields = ('nombre', 'email')