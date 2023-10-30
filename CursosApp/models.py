<<<<<<< HEAD
from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="cursos", null=True, blank=True)
    descripcion = models.TextField(max_length=500)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.nombre
    

# Modelo para la tabla de Unidades de un Curso
class UnidadCurso(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    orden = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo

# Modelo para la tabla de Videos relacionados con las unidades
class Video(models.Model):
    unidad = models.ForeignKey(UnidadCurso, on_delete=models.CASCADE)
    
    titulo = models.CharField(max_length=255)
    video_url = models.URLField()
    descripcion = models.TextField()

    def __str(self):
        return self.titulo

# Modelo para la tabla de Actividades relacionadas con las unidades
class Actividad(models.Model):
    unidad = models.ForeignKey(UnidadCurso, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_entrega = models.DateField()
    tipo_actividad = models.CharField(max_length=50)
    ponderacion = models.DecimalField(max_digits=5, decimal_places=2)
    archivo_adjunto = models.FileField(upload_to='actividades/', null=True, blank=True)
    requisitos = models.TextField()
    calificacion_maxima = models.DecimalField(max_digits=5, decimal_places=2)
    enlace_externo = models.URLField(null=True, blank=True)
    notas_instructor = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre

# Modelo para la tabla de Quizzes
class Quizz(models.Model):
    unidad = models.ForeignKey(UnidadCurso, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    preguntas = models.ManyToManyField('Pregunta', related_name='quizzes')

    def __str__(self):
        return self.titulo

# Modelo para la tabla de Preguntas
class Pregunta(models.Model):
    texto_pregunta = models.TextField()
    opciones_respuesta = models.ManyToManyField('OpcionRespuesta', related_name='preguntas')
    respuesta_correcta = models.ForeignKey('OpcionRespuesta', on_delete=models.CASCADE)

    def __str__(self):
        return self.texto_pregunta

# Modelo para la tabla de Opciones de Respuesta
class OpcionRespuesta(models.Model):
    texto_respuesta = models.CharField(max_length=255)

    def __str__(self):
        return self.texto_respuesta

    


=======
from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="cursos", null=True, blank=True)
    descripcion = models.TextField(max_length=500)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
>>>>>>> 5189778f4bdd2befd384954f6d9a536dfc723bbd
