# Generated by Django 2.0.3 on 2018-04-06 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entrance', '0067_3_add_default_categories_20180406_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entranceexamtask',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='tasks',
                                    to='entrance.EntranceExamTaskCategory',
                                    verbose_name='категория'),
        ),
    ]
