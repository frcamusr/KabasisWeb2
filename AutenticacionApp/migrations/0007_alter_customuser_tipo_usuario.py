<<<<<<< HEAD
# Generated by Django 3.2.22 on 2023-10-19 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutenticacionApp', '0006_alter_customuser_tipo_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='tipo_usuario',
            field=models.CharField(blank=True, choices=[('', 'Selecciona el tipo de usuario'), ('editor_contenido', 'Editor de contenido'), ('revisor', 'Revisor'), ('estudiante', 'Estudiante'), ('visualizador', 'Visualizador'), ('reporteria', 'Reporteria'), ('administrador_empresa', 'Administrador empresa')], default='', max_length=50, verbose_name='Tipo de Usuario'),
        ),
    ]
=======
# Generated by Django 3.2.22 on 2023-10-19 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutenticacionApp', '0006_alter_customuser_tipo_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='tipo_usuario',
            field=models.CharField(blank=True, choices=[('', 'Selecciona el tipo de usuario'), ('editor_contenido', 'Editor de contenido'), ('revisor', 'Revisor'), ('estudiante', 'Estudiante'), ('visualizador', 'Visualizador'), ('reporteria', 'Reporteria'), ('administrador_empresa', 'Administrador empresa')], default='', max_length=50, verbose_name='Tipo de Usuario'),
        ),
    ]
>>>>>>> 5189778f4bdd2befd384954f6d9a536dfc723bbd
