# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-25 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuickServe', '0004_remove_purchases_justification'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchases',
            name='justification',
            field=models.ImageField(null=True, upload_to='%Y/%m/%d'),
        ),
    ]
