# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-31 08:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fangtan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='duixiang',
            name='elseinfo',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='report',
            name='report_to',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fangtan.duixiang'),
            preserve_default=False,
        ),
    ]
