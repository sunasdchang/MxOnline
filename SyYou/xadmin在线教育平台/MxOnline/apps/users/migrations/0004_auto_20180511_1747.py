# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-11 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180511_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(max_length=500, upload_to='banner/%Y/%m', verbose_name='轮播图'),
        ),
    ]
