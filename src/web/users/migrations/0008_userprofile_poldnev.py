# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 11:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poldnev', '0007_auto_20170318_1027'),
        ('users', '0007_auto_20170306_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='poldnev_person',
            field=models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_profiles', to='poldnev.Person'),
        ),
    ]
