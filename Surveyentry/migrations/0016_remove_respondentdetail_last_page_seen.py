# Generated by Django 3.1.1 on 2022-05-02 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Surveyentry', '0015_respondentdetail_last_page_seen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respondentdetail',
            name='last_page_seen',
        ),
    ]
