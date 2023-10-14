from django.db import models

# Create your models here.
class Cliente(models.Model):
    TIPO_CLIENTE = (
        ('PAR', 'Particular'),
        ('PRO', 'Profesional')
    )

    nombre = models.CharField(max_length=256, default="")
    domicilio = models.CharField(max_length=256, default="")
    cp = models.IntegerField(null=True, default=0, blank=True)
    ciudad = models.CharField(max_length=256, default="")
    telefono = models.CharField(max_length=256, default="")
    tipo = models.CharField(choices=TIPO_CLIENTE, default='PAR', max_length=3, null=False)
    nif = models.CharField(max_length=256, default="", null=True, blank=True)

    class Meta:
        ordering = ['pk']
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"