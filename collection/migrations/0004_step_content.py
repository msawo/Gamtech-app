# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-30 05:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0003_auto_20161230_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='content',
            field=models.TextField(blank=True, default=''),
        ),
    ]
