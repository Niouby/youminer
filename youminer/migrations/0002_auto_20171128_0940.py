# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youminer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='channel',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='video',
            name='created_date',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='video',
            name='image',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='video',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
    ]
