from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from Clientes.models import Cliente

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            dni = form.cleaned_data.get('dni')
            # Se chequea que el dni sea de un cliente existente
            cliente =  Cliente.objects.get(customer_dni = dni)
            if not cliente:
                form.errors['dni'] = ['El DNI no pertenece a ningún cliente.']
                return render(request, 'registration/signup.html', {'form': form})
            # Se agrega el customer id del cliente encontrado al usuario
            user = form.save(commit = False)
            user.customer_id = cliente
            user.save()
            # Se autentica y loguea al usuario
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})