from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

# Create your views here.
class IndexView(LoginRequiredMixin, generic.TemplateView):
  template_name = 'Clientes/index.html'