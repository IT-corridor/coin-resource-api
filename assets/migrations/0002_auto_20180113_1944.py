# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-13 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='buy_price',
            field=models.DecimalField(decimal_places=12, default=0.0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='asset',
            name='purchase_price',
            field=models.DecimalField(decimal_places=12, default=0.0, max_digits=20),
        ),
    ]