# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poldnev', '0003_auto_20170212_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='poldnev_role',
            field=models.CharField(help_text='Строка, обозначающая роль на poldnev.ru. Заполняется автоматически командой manage.py update_poldnev по информации с сайта.', max_length=150),
        ),
    ]
