# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-12 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizador', '0005_auto_20180712_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thermogenius',
            name='image',
            field=models.ImageField(default='', upload_to='thermo/'),
        ),
    ]
