from django.urls import path

from CursosApp import views

urlpatterns = [
    
    path('',views.cursos, name="Cursos"),
    
    path('agregar_curso/', views.agregar_curso, name="agregar_curso"),

    path('listar_curso/', views.listar_curso, name="listar_curso"),

    path('modificar_curso/<id>/', views.modificar_curso, name="modificar_curso"),

    path('eliminar_curso/<id>/', views.eliminar_curso, name="eliminar_curso"),

]

