# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-08 23:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20180106_0202'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='investment_start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]