# Generated by Django 4.2.5 on 2023-09-28 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutenticacionApp', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='usuarios', verbose_name='Imagen de Perfil'),
        ),
    ]
