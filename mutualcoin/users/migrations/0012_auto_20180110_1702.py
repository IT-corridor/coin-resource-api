# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-10 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20180110_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='investment_start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
