# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-09 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejudge', '0012_auto_20170405_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='solutioncheckingresult',
            name='report',
            field=models.TextField(blank=True),
        ),
    ]