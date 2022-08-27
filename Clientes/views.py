from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from rest_framework import generics
from .permissions import IsOwnerAndAuthenticated
from .serializers import ClienteSerializer
from .models import Cliente

# Create your views here.
class IndexView(LoginRequiredMixin, generic.TemplateView):
  template_name = 'Clientes/index.html'

class ClienteRetrieveView(generics.RetrieveAPIView):
  permission_classes = [IsOwnerAndAuthenticated]
  serializer_class = ClienteSerializer
  lookup_field = 'customer_id'
  queryset = Cliente.objects.all()