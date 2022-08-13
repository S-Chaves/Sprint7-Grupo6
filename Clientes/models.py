from django.db import models

# Create your models here.
class TipoCliente(models.Model):
    tipo = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_cliente'

class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()
    tipo_cliente = models.ForeignKey(TipoCliente, on_delete=models.DO_NOTHING, db_column='tipo_cliente')

    class Meta:
        managed = False
        db_table = 'cliente'

class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'empleado'