# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-17 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20180717_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart2',
            name='product',
            field=models.ImageField(blank=True, null=True, upload_to='picture'),
        ),
    ]
