# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-01 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProducaoUsina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.TimeField()),
                ('valor', models.FloatField()),
            ],
        ),
    ]
