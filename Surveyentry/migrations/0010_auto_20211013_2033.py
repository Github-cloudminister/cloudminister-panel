# Generated by Django 3.1.1 on 2021-10-13 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Surveyentry', '0009_auto_20210926_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='respondentsupplierdetail',
            name='supplier_internal_terminate_redirect_url',
            field=models.URLField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='respondentsupplierdetail',
            name='supplier_terminate_no_project_available',
            field=models.URLField(blank=True, default='', null=True),
        ),
    ]
