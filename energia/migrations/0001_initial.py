# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-01 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DadosCOSERN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarifa', models.FloatField()),
                ('importe', models.FloatField()),
                ('valor_fatura', models.FloatField()),
                ('injetado_fv', models.FloatField()),
                ('tributo_federal', models.FloatField()),
                ('consumo_energia_ativa_na_ponta_qtd', models.FloatField()),
                ('consumo_energia_ativa_na_ponta_valor', models.FloatField()),
                ('consumo_energia_ativa_fora_ponta_qtd', models.FloatField()),
                ('consumo_energia_ativa_fora_ponta_valor', models.FloatField()),
            ],
        ),
    ]
