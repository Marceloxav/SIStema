# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-15 18:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0002_auto_20170515_1800'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='abstractquestionnaireblock',
            options={'ordering': ('questionnaire_id', 'order'), 'verbose_name': 'questionnaire block'},
        ),
    ]
