from django.db import models

# Create your models here.

class Estudiante(models.Model):
    EstudianteID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    FechaNacimiento = models.DateField()
    Direccion = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=15)
    CorreoElectronico = models.EmailField()

class Profesor(models.Model):
    ProfesorID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    FechaNacimiento = models.DateField()
    Telefono = models.CharField(max_length=15)
    CorreoElectronico = models.EmailField()
    Especialidad = models.CharField(max_length=50)

class Administrativo(models.Model):
    AdministrativoID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=15)
    CorreoElectronico = models.EmailField()
    Puesto = models.CharField(max_length=50)

class Curso(models.Model):
    CursoID = models.AutoField(primary_key=True)
    NombreCurso = models.CharField(max_length=50)

class Asignatura(models.Model):
    AsignaturaID = models.AutoField(primary_key=True)
    NombreAsignatura = models.CharField(max_length=50)

class Calificacion(models.Model):
    CalificacionID = models.AutoField(primary_key=True)
    EstudianteID = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    AsignaturaID = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    ProfesorID = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    Nota = models.DecimalField(max_digits=4, decimal_places=2)
    FechaCalificacion = models.DateField()










