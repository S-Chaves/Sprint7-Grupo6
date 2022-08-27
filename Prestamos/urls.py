from django.urls import path
from .views import PrestamosView, PrestamoListView

urlpatterns = [
    path('api/prestamos/<int:pk>/', PrestamoListView.as_view()),
    path('prestamos/', PrestamosView.as_view(), name = 'prestamos')
]