# Generated by Django 4.2.11 on 2024-04-22 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0002_rename_descrucao_servico_descricao_servico_oficina_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordemservico',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Aberto'), (2, 'Concluído')], default=1, verbose_name='Status'),
        ),
    ]