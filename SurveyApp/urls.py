from django.urls import path
from . import views

urlpatterns = [
    path('crear_pregunta/', views.create_question, name='crear_pregunta'),
    path('preguntas/', views.preguntas, name='preguntas'),
    path('formulario/', views.formulario, name='formulario'),
    path('agradecimientos/', views.agradecimientos, name='agradecimientos'),
    # delete_question
    path('delete_question/<int:id>/', views.delete_question, name='delete_question'),
    # actualizar pregunta usando el mismo formulario de crear pregunta
    path('update_question/<int:id>/', views.update_question, name='update_question'),    
]

