# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-05 23:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuickServe', '0021_tabs_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabs',
            name='total',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
