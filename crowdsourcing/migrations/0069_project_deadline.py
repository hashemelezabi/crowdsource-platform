# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-16 07:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0068_worker_scope'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='deadline',
            field=models.DateTimeField(null=True),
        ),
    ]
