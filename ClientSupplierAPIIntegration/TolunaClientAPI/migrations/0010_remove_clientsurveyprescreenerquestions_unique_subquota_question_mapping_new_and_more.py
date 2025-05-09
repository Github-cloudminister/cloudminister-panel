# Generated by Django 4.0.6 on 2023-08-16 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0008_parentquestion_is_routable_and_more'),
        ('TolunaClientAPI', '0009_surveyentrytop7questions_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='clientsurveyprescreenerquestions',
            name='unique_subquota_question_mapping_new',
        ),
        migrations.RemoveField(
            model_name='clientsurveyprescreenerquestions',
            name='client_answer_mappings',
        ),
        migrations.RemoveField(
            model_name='clientsurveyprescreenerquestions',
            name='client_question_mapping',
        ),
        migrations.AddField(
            model_name='clientsurveyprescreenerquestions',
            name='age_range_list',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='clientsurveyprescreenerquestions',
            name='client_answer_mappings1',
            field=models.ManyToManyField(blank=True, editable=False, to='Questions.translatedanswer'),
        ),
        migrations.AddField(
            model_name='clientsurveyprescreenerquestions',
            name='client_question_mapping1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Questions.translatedquestion'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clientsurveyprescreenerquestions',
            name='allowedRangeMax',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='clientsurveyprescreenerquestions',
            name='allowedRangeMin',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
