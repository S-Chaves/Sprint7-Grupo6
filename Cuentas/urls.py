from django.urls import path
from .views import CuentaListView

urlpatterns = [
  path('cuentas/<int:pk>/', CuentaListView.as_view())
]