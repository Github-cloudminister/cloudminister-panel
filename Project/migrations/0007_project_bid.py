# Generated by Django 3.1.1 on 2021-07-15 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bid', '0001_initial'),
        ('Project', '0006_auto_20210715_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='Bid',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bid', to='Bid.bid'),
        ),
    ]
