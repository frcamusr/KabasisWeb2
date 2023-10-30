from django.shortcuts import render, redirect, get_object_or_404

from .forms import CursoForm

from .models import Curso

from django.contrib import messages

# Create your views here.

def cursos(request):

    return render(request, "CursosApp/cursos.html")

def agregar_curso(request):

    data = {
        'form': CursoForm()

    }

    if request.method == 'POST':
        formulario = CursoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Curso creado con éxito.')
        else: 
            data["form"] = formulario
    
    return render(request, "CursosApp/agregar_curso.html", data)

def listar_curso(request):
    cursos = Curso.objects.all()

    data = {
        'cursos': cursos
    }

    return render(request, "CursosApp/listar_curso.html", data)


def modificar_curso(request, id):

    curso = get_object_or_404(Curso, id=id)

    data= {
        'form': CursoForm(instance = curso)
    }

    if request.method == 'POST':
        formulario = CursoForm(data=request.POST, instance=curso, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Curso actualizado correctamente")
            return redirect(to="listar_curso")
        
        data["form"] = formulario
    
    return render(request, "CursosApp/modificar_curso.html", data)

def eliminar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    curso.delete()
    return redirect(to="listar_curso")