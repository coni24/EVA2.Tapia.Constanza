from django.shortcuts import render,redirect
from EntradaApp.models import Entrada
from EntradaApp.forms import FormEntrada

def index(request):
    return render(request,'templateApp/index.html')

def listaEntrada(request):
    entradas = Entrada.objects.all()
    data = {'entradas': entradas}
    return render(request,'templateApp/entradas.html',data)

def agregarEntrada(request):
    form = FormEntrada()
    if request.method == 'POST':
        form = FormEntrada(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request,'templateApp/agregarEntrada.html',data)

def eliminarEntrada(request,id):
    entrada = Entrada.objects.get(id = id)
    entrada.delete()
    return redirect('/entradas')

def actualizarEntrada(request,id):
    entrada = Entrada.objects.get(id = id)
    form = FormEntrada(instance=entrada)
    if request.method == 'POST':
        form = FormEntrada(request.POST,instance=entrada)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request,'templateApp/agregarEntrada.html',data)
