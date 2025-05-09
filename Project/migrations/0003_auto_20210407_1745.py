# Generated by Django 3.1.1 on 2021-04-07 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0002_auto_20210305_0210'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectgroupsupplier',
            name='created_from_supplier_dashboard',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_revenue_month',
            field=models.CharField(choices=[('1', 'January'), ('2', 'February'), ('3', 'March'), ('4', 'April'), ('5', 'May'), ('6', 'June'), ('7', 'July'), ('8', 'August'), ('9', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')], default=4, max_length=2),
        ),
    ]
