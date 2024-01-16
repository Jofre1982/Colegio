from django.contrib import admin
from notas.models import Estudiante, Profesor, Administrativo, Asignatura, Calificacion, Curso

# Register your models here.

class EstudianteAdmin(admin.ModelAdmin):
    list_display=("Nombre", "Apellido")
    search_fields=("Nombre", "Apellido")

class ProfesorAdmin(admin.ModelAdmin):
    list_display=("Nombre", "Apellido")
    search_fields=("Nombre", "Apellido"," Especialidad")

class AdministrativoAdmin(admin.ModelAdmin):
    list_display=("Nombre", "Apellido")
    search_fields=("Nombre", "Apellido"," Puesto")
    


admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Administrativo, AdministrativoAdmin)
admin.site.register(Asignatura)
admin.site.register(Calificacion)
admin.site.register(Curso)

