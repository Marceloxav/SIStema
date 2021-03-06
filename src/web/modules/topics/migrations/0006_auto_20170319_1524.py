# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0005_auto_20170318_2110'),
        ('topics', '0005_filltopicsquestionnaireentrancestep_squashed_0007_auto_20170316_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scale',
            name='short_name',
            field=models.CharField(help_text='Используется в урлах. Лучше обойтись латинскими буквами, цифрами и подчёркиванием', max_length=100),
        ),
        migrations.AlterField(
            model_name='tag',
            name='short_name',
            field=models.CharField(help_text='Используется в урлах. Лучше обойтись латинскими буквами, цифрами и подчёркиванием', max_length=100),
        ),
        migrations.AlterField(
            model_name='topic',
            name='short_name',
            field=models.CharField(help_text='Используется в урлах. Лучше обойтись латинскими буквами, цифрами и подчёркиванием', max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='scale',
            unique_together=set([('questionnaire', 'short_name')]),
        ),
        migrations.AlterUniqueTogether(
            name='topic',
            unique_together=set([('questionnaire', 'short_name')]),
        ),
    ]
