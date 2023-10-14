from django.db import models
from cliente.models import Cliente

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=256, unique=True)
    cantidad = models.IntegerField(default=0)
    precio = models.FloatField(default=0.0)
    descuento = models.FloatField(default=0.0)

    class Meta:
        ordering = ['pk']
        verbose_name = "Libro"
        verbose_name_plural = "Libros"

class Linea(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.RESTRICT)
    cantidad = models.IntegerField(default=0)
    pvp = models.FloatField(default=0.0)
    precio = models.FloatField(default=0.0)
    importe_total = models.FloatField(default=0.0)

    class Meta:
        ordering = ['pk']
        verbose_name = "Línea Factura/Pedido"
        verbose_name_plural = "Líneas Factura/Pedido"

class Factura(models.Model):
    FORMA_COBRO = (
        ('TAR', 'Tarjeta'),
        ('TRA', 'Transferencia')
    )

    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    fecha_pedido = models.DateField(null=True, blank=True)
    fecha_ingreso = models.DateField(null=True, blank=True)
    lineas = models.ManyToManyField(Linea)
    precio_total_sin_iva = models.FloatField(default=0.0)
    precio_total_iva = models.FloatField(default=0.0)
    descuento = models.FloatField(default=0.0)
    gastos_envio = models.FloatField(default=0.0)
    forma_cobro = models.CharField(choices=FORMA_COBRO, default='TAR', max_length=3)
    ingreso_banco = models.FloatField(default=0.0)
    recargo_equivalencia = models.FloatField(default=0.0)

    class Meta:
        ordering = ['pk']
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"
    
class Pedido(models.Model):
    FORMA_COBRO = (
            ('TAR', 'Tarjeta'),
            ('TRA', 'Transferencia')
        )

    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    fecha_pedido = models.DateField(null=True, blank=True)
    fecha_ingreso = models.DateField(null=True, blank=True)
    lineas = models.ManyToManyField(Linea)
    precio_total_sin_iva = models.FloatField(default=0.0)
    precio_total_iva = models.FloatField(default=0.0)
    descuento = models.FloatField(default=0.0)
    gastos_envio = models.FloatField(default=0.0)
    forma_cobro = models.CharField(choices=FORMA_COBRO, default='TAR', max_length=3)
    ingreso_banco = models.FloatField(default=0.0)
    recargo_equivalencia = models.FloatField(default=0.0)

    class Meta:
        ordering = ['pk']
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"