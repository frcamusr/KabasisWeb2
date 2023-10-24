from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="cursos", null=True, blank=True)
    descripcion = models.TextField(max_length=500)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

