# Generated by Django 4.0.6 on 2023-12-21 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0048_projectgroup_ad_enable_panel_projectgroupsubsupplier'),
        ('Surveyentry', '0043_respondentdetail_client_landing_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='respondenturldetail',
            name='sub_sup_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='RespondentProjectGroupSubSupplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_group_sub_supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Project.projectgroupsubsupplier')),
                ('respondent', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Surveyentry.respondentdetail')),
            ],
        ),
    ]
