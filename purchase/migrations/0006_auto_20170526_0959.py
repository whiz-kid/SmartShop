# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 09:59
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('purchase', '0005_auto_20170526_0956'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(default=datetime.datetime(2017, 5, 26, 9, 59, 43, 213725, tzinfo=utc))),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchase.Item')),
            ],
        ),
        migrations.AlterField(
            model_name='cart',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 26, 9, 59, 43, 212506, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 26, 9, 59, 43, 213111, tzinfo=utc)),
        ),
    ]