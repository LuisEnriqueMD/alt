# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-12 23:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizador', '0006_auto_20180712_1726'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='especifications',
            options={'ordering': ('name',), 'verbose_name': 'Especificaci\xf3n', 'verbose_name_plural': 'Especificaciones'},
        ),
    ]
