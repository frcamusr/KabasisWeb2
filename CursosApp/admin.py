from django.contrib import admin
from .models import Curso

# Register your models here.


class CursoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Curso)