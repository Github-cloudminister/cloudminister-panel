# Generated by Django 3.1.1 on 2021-11-29 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Invoice', '0004_auto_20211026_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_status',
            field=models.CharField(choices=[('1', 'Draft'), ('2', 'Sent'), ('3', 'Paid'), ('4', 'Cancel')], default='1', max_length=1),
        ),
    ]
