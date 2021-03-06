# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 04:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0002_auto_20170524_0635'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='customer_name',
            new_name='customer',
        ),
        migrations.AlterField(
            model_name='cart',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 25, 4, 23, 30, 576185, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='item',
            name='logo',
            field=models.CharField(default='../../static/purchase/images/', max_length=500),
        ),
    ]
