from django.shortcuts import render, redirect, get_object_or_404
from .models import Registro
from .forms import RegistroForm

# Vista para listar todos los registros
def lista_registros(request):
    registros = Registro.objects.all()  # Obtener todos los registros de la BD
    return render(request, 'client/lista.html', {'registros': registros})


# Vista para crear un nuevo registro
def crear_registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda en la base de datos
            return redirect('lista')  # Redirecciona a la lista después de guardar
    else:
        form = RegistroForm()
    return render(request, 'client/formulario.html', {'form': form})


# Vista para actualizar un registro existente
def actualizar_registro(request, pk):
    registro = get_object_or_404(Registro, pk=pk)  # Si no existe, lanza 404
    form = RegistroForm(request.POST or None, instance=registro)
    if form.is_valid():
        form.save()
        return redirect('lista')
    return render(request, 'client/formulario.html', {'form': form})