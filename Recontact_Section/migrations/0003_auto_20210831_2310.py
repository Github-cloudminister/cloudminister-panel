# Generated by Django 3.1.1 on 2021-08-31 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recontact_Section', '0002_auto_20210808_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recontact',
            name='pid',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='recontact',
            name='rid',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
