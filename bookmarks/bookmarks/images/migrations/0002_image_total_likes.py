# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 01:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='total_likes',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
    ]
