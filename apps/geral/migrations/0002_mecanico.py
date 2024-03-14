# Generated by Django 5.0.3 on 2024-03-12 00:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geral', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mecanico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('codigo', models.PositiveSmallIntegerField(verbose_name='Código')),
                ('oficna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geral.oficina', verbose_name='Oficina')),
            ],
            options={
                'verbose_name': 'Mecânico',
                'verbose_name_plural': 'Mecânicos',
                'ordering': ['nome'],
            },
        ),
    ]