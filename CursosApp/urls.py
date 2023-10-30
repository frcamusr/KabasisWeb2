from django.urls import path

from CursosApp import views

urlpatterns = [
    
<<<<<<< HEAD
    path('',views.cursos, name="Cursos"),
    
    path('agregar_curso/', views.agregar_curso, name="agregar_curso"),

    path('listar_curso/', views.listar_curso, name="listar_curso"),
=======
    path('grwt/',views.cursos, name="Cursos"),
    
    path('agregar_curso/', views.agregar_curso, name="agregar_curso"),

    path('', views.listar_curso, name="listar_curso"),
>>>>>>> 5189778f4bdd2befd384954f6d9a536dfc723bbd

    path('modificar_curso/<id>/', views.modificar_curso, name="modificar_curso"),

    path('eliminar_curso/<id>/', views.eliminar_curso, name="eliminar_curso"),

<<<<<<< HEAD
    path('ver_curso/<id>/', views.ver_curso, name='ver_curso'),



    path('agregar_unidad/', views.agregar_unidad, name="agregar_unidad"),

    path('listar_unidad/<id>/', views.listar_unidad, name="listar_unidad"),

    path('eliminar_unidad/<id>/', views.eliminar_unidad, name="eliminar_unidad"),

    path('modificar_unidad/<id>/', views.modificar_unidad, name="modificar_unidad"),

=======
>>>>>>> 5189778f4bdd2befd384954f6d9a536dfc723bbd
]

