from django.contrib import admin
from .models import Curso, UnidadCurso, Video, Actividad, Quizz, Pregunta, OpcionRespuesta

# Register your models here.


class CursoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Curso)

@admin.register(UnidadCurso)
class UnidadCursoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'titulo', 'orden')
    
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('unidad', 'titulo')
    
@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ('unidad', 'nombre', 'tipo_actividad')
    
@admin.register(Quizz)
class QuizzAdmin(admin.ModelAdmin):
    list_display = ('unidad', 'titulo')
    
@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('texto_pregunta',)

@admin.register(OpcionRespuesta)
class OpcionRespuestaAdmin(admin.ModelAdmin):
    list_display = ('texto_respuesta',)