# Generated by Django 4.2.11 on 2024-04-12 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geral', '0002_mecanico'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mecanico',
            old_name='oficna',
            new_name='oficina',
        ),
    ]
