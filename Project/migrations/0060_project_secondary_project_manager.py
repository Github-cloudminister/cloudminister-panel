# Generated by Django 4.0.6 on 2024-06-20 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Project', '0059_alter_project_project_revenue_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='secondary_project_manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='secondary_project_manager', to=settings.AUTH_USER_MODEL),
        ),
    ]
