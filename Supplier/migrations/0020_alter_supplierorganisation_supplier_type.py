# Generated by Django 4.0.6 on 2023-11-24 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supplier', '0019_suppliercontact_supplier_mail_sent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplierorganisation',
            name='supplier_type',
            field=models.CharField(choices=[('1', 'Manual'), ('2', 'API'), ('3', 'Router'), ('4', 'Panel'), ('5', 'Panel 2')], default='1', max_length=1),
        ),
    ]
