from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Prestamo
from Clientes.models import Cliente

# Create your views here.
class PrestamosView(LoginRequiredMixin, generic.DetailView):
  model = Prestamo

  def get(self, request):
    user = request.user.customer_id
    prestamos = Prestamo.objects.filter(customer_id = user.customer_id)
    
    return render(request, 'Prestamos/prestamos.html', { 'prestamos': prestamos })
  
  def post(self, request):
    user = request.user.customer_id
    cliente = Cliente.objects.get(customer_id = user.customer_id)
    tipo_cliente = cliente.tipo_cliente.tipo

    tipo_prestamo = request.POST['tipo'].upper()
    fecha = request.POST['fecha']
    monto = int(request.POST['monto'])

    if tipo_cliente == 'Classic' and monto > 100000:
      error = 'El monto seleccionado excede el límite de tu tipo de cuenta.'
      return render(request, 'Prestamos/prestamos.html', { 'error': error })
    elif tipo_cliente == 'Gold' and monto > 300000:
      error = 'El monto seleccionado excede el límite de tu tipo de cuenta.'
      return render(request, 'Prestamos/prestamos.html', { 'error': error })
    elif tipo_cliente == 'Black' and monto > 500000:
      error = 'El monto seleccionado excede el límite de tu tipo de cuenta.'
      return render(request, 'Prestamos/prestamos.html', { 'error': error })

    prestamo = Prestamo(loan_type = tipo_prestamo, loan_date = fecha,
     loan_total = monto, customer_id = user.customer_id)
    prestamo.save()

    return redirect('index') 