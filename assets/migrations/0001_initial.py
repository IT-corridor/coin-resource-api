# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-13 19:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('symbol', models.CharField(default='', max_length=200)),
                ('image_url', models.CharField(default='', max_length=200)),
                ('amount', models.DecimalField(decimal_places=16, default=0.0, max_digits=20)),
                ('currency', models.CharField(default='', max_length=10)),
                ('price_type', models.CharField(default='', max_length=10)),
                ('buy_price', models.DecimalField(decimal_places=16, default=0.0, max_digits=20)),
                ('purchase_price', models.DecimalField(decimal_places=20, default=0.0, max_digits=20)),
                ('sell_price', models.DecimalField(decimal_places=8, default=0.0, max_digits=20)),
                ('transaction_date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('note', models.CharField(blank=True, max_length=256, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-transaction_date',),
            },
        ),
        migrations.CreateModel(
            name='SoldAssets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('symbol', models.CharField(default='', max_length=200)),
                ('image_url', models.CharField(default='', max_length=200)),
                ('asset_id', models.CharField(default='', max_length=2)),
                ('purchase_price', models.DecimalField(decimal_places=16, default=0.0, max_digits=20)),
                ('amount', models.DecimalField(decimal_places=8, default=0.0, max_digits=10)),
                ('sell_price', models.DecimalField(decimal_places=8, default=0.0, max_digits=20)),
                ('market_price', models.DecimalField(decimal_places=8, default=0.0, max_digits=20)),
                ('currency', models.CharField(default='', max_length=10)),
                ('price_type', models.CharField(default='', max_length=10)),
                ('transaction_date', models.DateField(blank=True)),
                ('note', models.CharField(blank=True, max_length=256, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
