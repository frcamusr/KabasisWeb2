from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .forms import CustomUserCreationForm

# Create your views here.

def cerrar_sesion(request):
    logout(request)

    return redirect('Home')

def logear(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            usuario = authenticate(username = nombre_usuario, password = contra)
            if usuario is not None:
                login(request, usuario)
                messages.success(request, "Has iniciado sesión correctamente")
                return redirect('Home')
            else:
                messages.error(request, "usuario no valido")
        else:
            messages.error(request, "Información incorrecta")

    form = AuthenticationForm()

    
    return render(request, "login/login.html", {"form" : form})



def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST, request.FILES)  # Asegúrate de incluir request.FILES aquí
        if formulario.is_valid():
            user = formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado con éxito")
            return redirect(to="Home")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)





from .forms import UserProfileForm

@login_required
def view_profile(request):
    return render(request, 'registration/view_profile.html', {'user': request.user})



@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = UserProfileForm(instance=request.user)
    
    return render(request, 'registration/edit_profile.html', {'form': form})
