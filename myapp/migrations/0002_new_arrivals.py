# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-12 16:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='new_arrivals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='picture')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Categories')),
            ],
        ),
    ]