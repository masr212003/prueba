# Generated by Django 4.2.11 on 2024-10-24 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webprincipal', '0006_carritoproducto_precio_carritoproducto_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(default=2, upload_to='productos/'),
            preserve_default=False,
        ),
    ]