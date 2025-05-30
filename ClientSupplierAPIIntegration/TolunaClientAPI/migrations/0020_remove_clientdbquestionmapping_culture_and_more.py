# Generated by Django 5.0.6 on 2024-07-15 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TolunaClientAPI', '0019_clientquota_project_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientdbquestionmapping',
            name='culture',
        ),
        migrations.RemoveField(
            model_name='clientdbquestionmapping',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='clientdbquestionmapping',
            name='ques_category',
        ),
        migrations.RemoveField(
            model_name='surveyentrytop7questions',
            name='client_questions_mapping',
        ),
        migrations.RemoveField(
            model_name='clientquestioncategory',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='clientstudytype',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='projectgroupadditionalfields',
            name='study_type',
        ),
        migrations.RemoveField(
            model_name='projectgroupadditionalfields',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='projectgroupadditionalfields',
            name='project_group',
        ),
        migrations.RemoveField(
            model_name='clientquota',
            name='client_survey',
        ),
        migrations.RemoveField(
            model_name='projectgroupsupplieradditionalfields',
            name='prj_grp_supplier',
        ),
        migrations.DeleteModel(
            name='ClientDBAnswerMapping',
        ),
        migrations.DeleteModel(
            name='ClientDBQuestionMapping',
        ),
        migrations.DeleteModel(
            name='SurveyEntryTop7Questions',
        ),
        migrations.DeleteModel(
            name='ClientQuestionCategory',
        ),
        migrations.DeleteModel(
            name='ClientStudyType',
        ),
        migrations.DeleteModel(
            name='ProjectGroupAdditionalFields',
        ),
        migrations.DeleteModel(
            name='ProjectGroupSupplierAdditionalFields',
        ),
    ]
