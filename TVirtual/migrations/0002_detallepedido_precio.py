# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-24 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TVirtual', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallepedido',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=6),
            preserve_default=False,
        ),
    ]
