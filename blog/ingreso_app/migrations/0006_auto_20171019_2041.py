# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-19 20:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ingreso_app', '0005_auto_20171019_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 19, 20, 41, 19, 591462, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 19, 20, 41, 19, 590734, tzinfo=utc)),
        ),
    ]
