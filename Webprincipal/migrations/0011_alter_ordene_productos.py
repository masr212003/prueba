# Generated by Django 4.2.11 on 2024-10-29 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webprincipal', '0010_ordene_delete_orden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordene',
            name='productos',
            field=models.ManyToManyField(to='Webprincipal.carritoproducto'),
        ),
    ]