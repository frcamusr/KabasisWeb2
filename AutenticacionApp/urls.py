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

]

# urls.py

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL[1:], document_root=settings.MEDIA_ROOT)
