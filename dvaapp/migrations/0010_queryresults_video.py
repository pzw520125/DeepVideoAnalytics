# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 03:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0009_queryresults'),
    ]

    operations = [
        migrations.AddField(
            model_name='queryresults',
            name='video',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Video'),
            preserve_default=False,
        ),
    ]