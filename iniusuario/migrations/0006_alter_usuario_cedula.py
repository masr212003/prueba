# Generated by Django 4.2.11 on 2024-10-06 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iniusuario', '0005_alter_usuario_cedula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cedula',
            field=models.CharField(max_length=8),
        ),
    ]