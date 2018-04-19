# Generated by Django 2.0.3 on 2018-04-18 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dates', '0004_3_unique_school_and_short_name_20180323_2115'),
        ('entrance', '0073_entranceexamtaskcategory_is_mandatory'),
    ]

    operations = [
        migrations.AddField(
            model_name='entranceexamtaskcategory',
            name='available_from_time',
            field=models.ForeignKey(blank=True, default=None, help_text='Момент времени, начиная с которого задачи этой категории показываются пользователям. Оставьте пустым, если задачи должны быть доступны с начала вступительной работы.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='dates.KeyDate', verbose_name='доступна c'),
        ),
        migrations.AddField(
            model_name='entranceexamtaskcategory',
            name='available_to_time',
            field=models.ForeignKey(blank=True, default=None, help_text='Момент времени, после которого возможность послать решения по задачам этой категории будет закрыта. Оставьте пустым, если задачи должны быть доступны до конца вступительной работы.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='dates.KeyDate', verbose_name='доступна до'),
        ),
        migrations.AddField(
            model_name='entranceexamtaskcategory',
            name='text_after_closing',
            field=models.TextField(blank=True, help_text='Текст, который показывается на странице задачи после закрытия задач этой категории, но до конца вступительной работы.\nПоддерживается Markdown.', verbose_name='текст после закрытия'),
        ),
    ]
