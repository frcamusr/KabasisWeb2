from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    TIPO_USUARIO_CHOICES = (
        ('', 'Selecciona el tipo de usuario'),  # Opción en blanco
        ('editor_contenido', 'Editor de contenido'),
        ('revisor', 'Revisor'),
        ('estudiante', 'Estudiante'),
        ('visualizador', 'Visualizador'),
        ('reporteria', 'Reporteria'),
        ('administrador_empresa', 'Administrador empresa'),
    )

    tipo_usuario = models.CharField(
        max_length=50,
        choices=TIPO_USUARIO_CHOICES,
        default='',
        blank=True,
        verbose_name="Tipo de Usuario"
    )
    
    # Nuevo campo para la imagen de perfil
    profile_picture = models.ImageField(
        upload_to='usuarios/',  # Define la carpeta donde se guardarán las imágenes
        null=True,
        blank=True,
        verbose_name="Imagen de Perfil"
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Usuario Personalizado"
        verbose_name_plural = "Usuarios Personalizados"
