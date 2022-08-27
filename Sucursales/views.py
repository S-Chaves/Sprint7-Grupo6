from django.shortcuts import render
from rest_framework import generics
from .serializers import SucursalSerializer
from .models import Sucursal

# Create your views here.
class SucursalListView(generics.ListAPIView):
  serializer_class = SucursalSerializer
  queryset = Sucursal.objects.all()
