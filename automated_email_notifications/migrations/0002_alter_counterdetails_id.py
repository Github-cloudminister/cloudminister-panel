# Generated by Django 4.0.6 on 2022-08-03 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automated_email_notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counterdetails',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
