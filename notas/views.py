from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "notas/home.html")

def notas(request):
    return render(request, "notas/notas.html")

def profesor(request):
    return render(request, "notas/profesor.html")

def estudiante(request):
    return render(request, "notas/estudiante.html")

def asignatura(request):
    return render(request, "notas/asignatura.html")

def curso(request):
    return render(request, "notas/curso.html")

def calificacion(request):
    return render(request, "notas/calificacion.html")
