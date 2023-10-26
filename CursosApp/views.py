from django.shortcuts import render, redirect, get_object_or_404

from .forms import CursoForm, UnidadForm

from .models import Curso, UnidadCurso

from django.contrib import messages

# Create your views here.

def cursos(request):
    cursos = Curso.objects.all()
    data = {

        'cursos': cursos
    }
    return render(request, "CursosApp/cursos.html", data)

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
    messages.success(request, 'Curso eliminado con éxito.')
    return redirect(to="listar_curso")


from django.shortcuts import render


def ver_curso(request, id):
    curso = Curso.objects.get(pk=id)
    unidades = UnidadCurso.objects.filter(curso=curso).order_by('orden')
    
    data = {
        'curso': curso,
        'unidades': unidades,
    }
    
    return render(request, 'CursosApp/ver_curso.html', data)



############################## UNIDADES ######################################

from .forms import UnidadForm

def agregar_unidad(request):
    if request.method == 'POST':
        formulario = UnidadForm(request.POST, request.FILES)
        if formulario.is_valid():
            unidad = formulario.save(commit=False)  # No guardar inmediatamente para asignar curso
            curso_id = request.POST.get('curso')  # Asumiendo que el campo del formulario se llama 'curso'
            curso = Curso.objects.get(pk=curso_id)  # Obtén el curso correspondiente desde la base de datos
            # Concatenar el nombre del curso al título de la unidad
            unidad.titulo = f"{unidad.titulo}"
            unidad.curso = curso  # Asignar el curso al que pertenece esta unidad
            unidad.save()  # Ahora guarda la unidad con el curso asignado y el nombre modificado
            messages.success(request, 'Unidad creada con éxito.')
            formulario = UnidadForm() 
        else:
            messages.error(request, 'Error al crear la unidad. Por favor, verifica el formulario.')
    else:
        formulario = UnidadForm()

    data = {'form': formulario}
    return render(request, "unidades/agregar_unidad.html", data)

    
def listar_unidad(request, id):
    curso = Curso.objects.get(pk=id)
    unidades = UnidadCurso.objects.filter(curso=curso).order_by('orden')
    
    data = {
        'curso': curso,
        'unidades': unidades,
    }
    
    return render(request, 'unidades/listar_unidad.html', data)


def eliminar_unidad(request, id):
    unidad = get_object_or_404(UnidadCurso, pk=id)
    curso_id = unidad.curso.id  # Obtiene el ID del curso al que pertenece la unidad
    unidad.delete()
    
    # Modifica la siguiente línea para pasar el ID correctamente
    return redirect('listar_unidad', id=curso_id)




def modificar_unidad(request, id):
    unidad = get_object_or_404(UnidadCurso, id=id)
    curso_id = unidad.curso.id  # Obtiene el ID del curso al que pertenece la unidad

    data = {
        'form': UnidadForm(instance=unidad)
    }

    if request.method == 'POST':
        formulario = UnidadForm(data=request.POST, instance=unidad, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Unidad actualizada correctamente")
            
            # Redirige a la vista 'listar_unidad' con el ID del curso como parámetro
            return redirect('listar_unidad', id=curso_id)

        data["form"] = formulario

    return render(request, "unidades/modificar_unidad.html", data)



###




