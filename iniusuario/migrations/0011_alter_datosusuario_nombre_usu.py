# Generated by Django 4.2.11 on 2024-10-18 20:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('iniusuario', '0010_alter_datosusuario_nombre_usu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosusuario',
            name='nombre_usu',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
