from django.db import models

# Create your models here.
class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prestamo'

class Movimientos(models.Model):
    movimiento_id = models.AutoField(primary_key=True)
    numero_cuenta = models.IntegerField(blank=True, null=True)
    monto = models.IntegerField(blank=True, null=True)
    tipo_operacion = models.TextField(blank=True, null=True)
    hora = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'movimientos'
    