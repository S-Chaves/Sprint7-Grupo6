from django.urls import path
from . import views

urlpatterns = [
    path('', views.PrestamosView.as_view(), name = 'prestamos')
]