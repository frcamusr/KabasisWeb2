# Generated by Django 3.2.22 on 2023-10-30 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CursosApp', '0002_actividad_opcionrespuesta_pregunta_quizz_unidadcurso_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='archivo',
        ),
        migrations.AddField(
            model_name='video',
            name='video_url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
