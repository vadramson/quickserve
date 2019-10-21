# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-05 22:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('QuickServe', '0019_auto_20171005_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderNumber', models.CharField(blank=True, max_length=254, null=True)),
                ('dateOp', models.DateTimeField(blank=True, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=25, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]