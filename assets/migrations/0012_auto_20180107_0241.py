# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-07 02:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0011_auto_20180107_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='amount',
            field=models.DecimalField(decimal_places=8, default=0.0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='asset',
            name='buy_price',
            field=models.DecimalField(decimal_places=8, default=0.0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='asset',
            name='sell_price',
            field=models.DecimalField(decimal_places=8, default=0.0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='soldassets',
            name='market_price',
            field=models.DecimalField(decimal_places=8, default=0.0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='soldassets',
            name='sell_price',
            field=models.DecimalField(decimal_places=8, default=0.0, max_digits=20),
        ),
    ]
