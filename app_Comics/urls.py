from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_comics, name='inicio_comics'),
    
    # URLs para Producto
    path('productos/agregar/', views.agregar_Producto, name='agregar_Producto'),
    path('productos/', views.ver_Productos, name='ver_Productos'),
    path('productos/actualizar/<int:producto_id>/', views.actualizar_Producto, name='actualizar_Producto'),
    path('productos/realizar_actualizacion/<int:producto_id>/', views.realizar_actualizacion_Producto, name='realizar_actualizacion_Producto'),
    path('productos/borrar/<int:producto_id>/', views.borrar_Producto, name='borrar_Producto'),
    path('productos/confirmar_borrar/<int:producto_id>/', views.confirmar_borrar_Producto, name='confirmar_borrar_Producto'),
    
    # URLs para Proveedor
    path('proveedores/agregar/', views.agregar_Proveedor, name='agregar_Proveedor'),
    path('proveedores/', views.ver_Proveedores, name='ver_Proveedores'),
    path('proveedores/actualizar/<int:proveedor_id>/', views.actualizar_Proveedor, name='actualizar_Proveedor'),
    path('proveedores/realizar_actualizacion/<int:proveedor_id>/', views.realizar_actualizacion_Proveedor, name='realizar_actualizacion_Proveedor'),
    path('proveedores/borrar/<int:proveedor_id>/', views.borrar_Proveedor, name='borrar_Proveedor'),
    path('proveedores/confirmar_borrar/<int:proveedor_id>/', views.confirmar_borrar_Proveedor, name='confirmar_borrar_Proveedor'),
]