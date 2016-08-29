# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-08 02:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0091_auto_20160607_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='education',
            field=models.CharField(blank=True, choices=[(b'some_high', b'Some High School, No Degree'), (b'high', b'High School Degree or Equivalent'), (b'some_college', b'Some College, No Degree'), (b'associates', b'Associates Degree'), (b'bachelors', b'Bachelors Degree'), (b'masters', b'Graduate Degree, Masters'), (b'doctorate', b'Graduate Degree, Doctorate')], max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='income',
            field=models.CharField(blank=True, choices=[(b'less_1k', b'Less than $1,000'), (b'1k', b'$1,000 - $1,999'), (b'2.5k', b'$2,500 - $4,999'), (b'5k', b'$5,000 - $7,499'), (b'7.5k', b'$7,500 - $9,999'), (b'10k', b'$10,000 - $14,999'), (b'15k', b'$15,000 - $24,999'), (b'25k', b'$25,000 - $39,999'), (b'40k', b'$40,000 - $59,999'), (b'60k', b'$60,000 - $74,999'), (b'75k', b'$75,000 - $99,999'), (b'100k', b'$100,000 - $149,999'), (b'150k', b'$150,000 - $199,999'), (b'200k', b'$200,000 - $299,999'), (b'300k_more', b'$300,000 or more')], max_length=9, null=True),
        ),
    ]