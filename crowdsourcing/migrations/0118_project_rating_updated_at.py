# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-13 22:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0117_project_tasks_in_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='rating_updated_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 7, 13, 22, 57, 23, 300054, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
