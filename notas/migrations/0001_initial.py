# Generated by Django 5.0.1 on 2024-01-15 17:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrativo',
            fields=[
                ('AdministrativoID', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellido', models.CharField(max_length=50)),
                ('Telefono', models.CharField(max_length=15)),
                ('CorreoElectronico', models.EmailField(max_length=254)),
                ('Puesto', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('AsignaturaID', models.AutoField(primary_key=True, serialize=False)),
                ('NombreAsignatura', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('CursoID', models.AutoField(primary_key=True, serialize=False)),
                ('NombreCurso', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('EstudianteID', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellido', models.CharField(max_length=50)),
                ('FechaNacimiento', models.DateField()),
                ('Direccion', models.CharField(max_length=100)),
                ('Telefono', models.CharField(max_length=15)),
                ('CorreoElectronico', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('ProfesorID', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellido', models.CharField(max_length=50)),
                ('FechaNacimiento', models.DateField()),
                ('Telefono', models.CharField(max_length=15)),
                ('CorreoElectronico', models.EmailField(max_length=254)),
                ('Especialidad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('CalificacionID', models.AutoField(primary_key=True, serialize=False)),
                ('Nota', models.DecimalField(decimal_places=2, max_digits=4)),
                ('FechaCalificacion', models.DateField()),
                ('AsignaturaID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.asignatura')),
                ('EstudianteID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.estudiante')),
                ('ProfesorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.profesor')),
            ],
        ),
    ]