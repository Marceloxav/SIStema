# Generated by Django 2.0.3 on 2018-05-26 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_auto_20180312_2139'),
        ('enrolled_scans', '0008_auto_20180312_2139'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupEnrolledScanRequirementCondition',
            fields=[
                ('enrolledscanrequirementcondition_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='enrolled_scans.EnrolledScanRequirementCondition')),
                ('group', models.ForeignKey(help_text='Группа, участников которой надо попросить загрузить документ', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='groups.AbstractGroup')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('enrolled_scans.enrolledscanrequirementcondition',),
        ),
        migrations.AlterField(
            model_name='questionnairevariantenrolledscanrequirementcondition',
            name='variant',
            field=models.ForeignKey(help_text='Вариант, который должен быть отмечен, чтобы пользователя попросили загрузить документ', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='questionnaire.ChoiceQuestionnaireQuestionVariant'),
        ),
    ]