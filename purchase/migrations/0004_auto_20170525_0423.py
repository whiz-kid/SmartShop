# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 04:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0003_auto_20170525_0423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 25, 4, 23, 47, 225352, tzinfo=utc)),
        ),
    ]
