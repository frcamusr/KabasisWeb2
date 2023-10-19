from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import cerrar_sesion, registro



urlpatterns = [

    path('cerrar_sesion',cerrar_sesion, name="cerrar_sesion"),

    

    path('', registro, name= "registro"),

    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),


    path('usuarios_personalizados/', views.lista_usuarios_personalizados, name='lista_usuarios_personalizados'),
    path('usuarios_personalizados/crear/', views.crear_usuario_personalizado, name='crear_usuario_personalizado'),
    path('usuarios_personalizados/<int:id_usuario>/actualizar/', views.actualizar_usuario_personalizado, name='actualizar_usuario_personalizado'),
    path('usuarios_personalizados/<int:id_usuario>/eliminar/', views.eliminar_usuario_personalizado, name='eliminar_usuario_personalizado'),
]



# urls.py

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL[1:], document_root=settings.MEDIA_ROOT)
