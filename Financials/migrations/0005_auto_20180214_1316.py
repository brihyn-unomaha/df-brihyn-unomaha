# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-14 19:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Financials', '0004_auto_20180214_1257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cryptocurrency',
            old_name='cryptoname',
            new_name='crypto_name',
        ),
        migrations.RenameField(
            model_name='cryptocurrency',
            old_name='purchasedate',
            new_name='purchase_date',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customername',
            new_name='customer_name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='streetaddress',
            new_name='street_address',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='purchasedate',
            new_name='purchase_date',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='stockname',
            new_name='stock_name',
        ),
    ]
