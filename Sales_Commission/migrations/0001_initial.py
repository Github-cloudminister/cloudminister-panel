# Generated by Django 4.0.6 on 2023-05-17 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Customer', '0006_customerorganization_threat_potential_score'),
        ('Project', '0038_alter_project_project_type'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales_Commission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_commision_amount', models.IntegerField()),
                ('payment_date', models.DateField()),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Paid', 'Paid'), ('Cancelled', 'Cancelled')], max_length=225)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.currency')),
                ('sales_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sales_Commission_Rows',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Project.project')),
                ('sales_commision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sales_Commission.sales_commission')),
            ],
        ),
    ]
