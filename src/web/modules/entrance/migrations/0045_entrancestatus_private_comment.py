# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-13 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrance', '0044_auto_20170511_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrancestatus',
            name='private_comment',
            field=models.TextField(blank=True, help_text='Приватный комментарий. Виден только админам вступительной'),
        ),
    ]
