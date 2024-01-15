from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Home')

def notas(request):
    return HttpResponse('Notas')

def profesor(request):
    return HttpResponse('Profesor')

def estudiante(request):
    return HttpResponse('Estudiante')

def asignatura(request):
    return HttpResponse('Asignatura')

def curso(request):
    return HttpResponse('Curso')

def calificacion(request):
    return HttpResponse('Calificacion')
