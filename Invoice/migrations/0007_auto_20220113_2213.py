# Generated by Django 3.1.1 on 2022-01-13 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Invoice', '0006_auto_20211213_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='discount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='invoice',
            name='subtotal_after_discount',
            field=models.FloatField(default=0),
        ),
    ]
