from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'imagen', 'descripcion']

    def __init__(self, *args, **kwargs):
        super(CursoForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'  # Agregar la clase 'form-control' a cada campo

            if field_name == 'nombre':
                field.widget.attrs['placeholder'] = 'Nombre del curso'  # Agregar un marcador de posición para el campo 'nombre'

            # Puedes personalizar más cada campo si es necesario

