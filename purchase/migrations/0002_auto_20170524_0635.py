# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 06:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='logo',
            field=models.CharField(default='../../static/images/', max_length=500),
        ),
        migrations.AlterField(
            model_name='cart',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 24, 6, 35, 0, 354791, tzinfo=utc)),
        ),
    ]
