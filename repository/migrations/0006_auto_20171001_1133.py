# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-01 03:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0005_auto_20170929_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='latest_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='server',
            name='server_status_id',
            field=models.IntegerField(choices=[(1, '上架'), (2, '在线'), (3, '离线'), (4, '下架')], default=1),
        ),
    ]
