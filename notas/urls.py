from django.urls import path
from notas import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('profesor', views.profesor, name="Profesor"),
    path('estudiante', views.estudiante, name="Estudiante"),
    path('administrativo', views.administrativo, name="Administrativo"),
    path('asignatura', views.asignatura, name="Asignatura"),
    path('curso', views.curso, name="Curso"),
    path('calificacion', views.calificacion, name="Calificacion"),
]