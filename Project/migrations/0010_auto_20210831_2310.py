# Generated by Django 3.1.1 on 2021-08-31 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0009_auto_20210830_0106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scrubprojectsupplier',
            name='project_group',
        ),
        migrations.AddField(
            model_name='project',
            name='scrubproject',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='scrubprojectsupplier',
            name='rejected_counts',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='scrubprojectsupplier',
            name='total_achieved_counts',
            field=models.IntegerField(default=0),
        ),
    ]
