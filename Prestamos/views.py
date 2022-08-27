from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Prestamo
from Clientes.models import Cliente
from rest_framework import generics, exceptions
from .permissions import IsAuthenticated
from .serializers import PrestamoSerializer

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
    prestamos = Prestamo.objects.filter(customer_id = user.customer_id)
    tipo_cliente = cliente.tipo_cliente.tipo

    tipo_prestamo = request.POST['tipo'].upper()
    fecha = request.POST['fecha']
    monto = int(request.POST['monto'])

    if tipo_cliente == 'Classic' and monto > 100000:
      error = 'El monto seleccionado excede el límite de tu tipo de cuenta.'
      return render(request, 'Prestamos/prestamos.html', { 'error': error, 'prestamos': prestamos })
    elif tipo_cliente == 'Gold' and monto > 300000:
      error = 'El monto seleccionado excede el límite de tu tipo de cuenta.'
      return render(request, 'Prestamos/prestamos.html', { 'error': error, 'prestamos': prestamos })
    elif tipo_cliente == 'Black' and monto > 500000:
      error = 'El monto seleccionado excede el límite de tu tipo de cuenta.'
      return render(request, 'Prestamos/prestamos.html', { 'error': error, 'prestamos': prestamos })

    prestamo = Prestamo(loan_type = tipo_prestamo, loan_date = fecha,
     loan_total = monto, customer_id = cliente)
    prestamo.save()

    return redirect('index')

class PrestamoListView(generics.ListAPIView):
  permission_classes = [IsAuthenticated]
  serializer_class = PrestamoSerializer

  def get_queryset(self):
    id = self.kwargs['pk']
    user_id = self.request.user.customer_id.customer_id
    prestamos = Prestamo.objects.filter(customer_id = id)
    
    if not prestamos.exists():
      raise exceptions.NotFound(detail="No encontrado.")
    if user_id != id:
      raise exceptions.PermissionDenied(detail="Usted no tiene permiso para realizar esta acción.")

    return prestamos