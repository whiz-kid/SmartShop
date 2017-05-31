# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 15:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0009_auto_20170529_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 30, 15, 3, 58, 920299, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 30, 15, 3, 58, 920899, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='like',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 30, 15, 3, 58, 921611, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 30, 15, 3, 58, 922202, tzinfo=utc)),
        ),
    ]