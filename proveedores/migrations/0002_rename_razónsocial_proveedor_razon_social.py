# Generated by Django 5.1.7 on 2025-03-09 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proveedor',
            old_name='RazónSocial',
            new_name='razon_social',
        ),
    ]
