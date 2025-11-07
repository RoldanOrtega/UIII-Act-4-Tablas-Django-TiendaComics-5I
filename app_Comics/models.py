from django.db import models

# -----------------------
# MODELO PROVEEDOR
# -----------------------
class Proveedor(models.Model):
    nombre_Empresa = models.CharField(max_length=100)
    nombre_Contacto = models.CharField(max_length=100)
    telefono_Contacto = models.CharField(max_length=15)
    email_Contacto = models.EmailField(unique=True)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_Empresa} - {self.nombre_Contacto}"


# -----------------------
# MODELO PRODUCTO
# -----------------------
class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    autor = models.CharField(max_length=100)
    editorial = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    tipo_producto = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return f"{self.nombre} - {self.autor}"


# ========================================== 
# MODELO: CLIENTE 
# ========================================== 
class Cliente(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='clientes')
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)
    pais = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre