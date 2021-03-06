# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-28 01:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0002_auto_20170927_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '资产记录表',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('phone', models.CharField(max_length=32, verbose_name='座机')),
                ('mobile', models.CharField(max_length=32, verbose_name='手机')),
            ],
            options={
                'verbose_name_plural': '用户表',
            },
        ),
        migrations.AddField(
            model_name='assetrecord',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='repository.UserProfile'),
        ),
        migrations.AddField(
            model_name='assetrecord',
            name='server_obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ar', to='repository.Server'),
        ),
    ]
