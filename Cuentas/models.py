from django.db import models

# Create your models here.
class TipoCuenta(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_cuenta'

class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    tipo_cuenta = models.ForeignKey(TipoCuenta, on_delete=models.DO_NOTHING, db_column='tipo_cuenta', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuenta'