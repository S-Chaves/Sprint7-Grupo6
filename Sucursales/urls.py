from django.urls import path
from .views import SucursalListView

urlpatterns = [
  path('', SucursalListView.as_view())
]