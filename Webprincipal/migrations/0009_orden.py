# Generated by Django 4.2.11 on 2024-10-29 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webprincipal', '0008_carritoproducto_preciofin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('productos', models.ManyToManyField(to='Webprincipal.productos')),
            ],
        ),
    ]
