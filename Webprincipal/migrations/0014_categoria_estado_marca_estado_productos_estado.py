# Generated by Django 4.2.11 on 2024-11-04 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webprincipal', '0013_ordene_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='estado',
            field=models.CharField(choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default='activo', max_length=12),
        ),
        migrations.AddField(
            model_name='marca',
            name='estado',
            field=models.CharField(choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default='activo', max_length=12),
        ),
        migrations.AddField(
            model_name='productos',
            name='estado',
            field=models.CharField(choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default='activo', max_length=12),
        ),
    ]
