# Generated by Django 4.0.6 on 2024-06-20 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0060_project_secondary_project_manager'),
        ('TolunaClientAPI', '0018_surveyqualifyparameterscheck'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientquota',
            name='project_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Project.projectgroup'),
        ),
    ]
