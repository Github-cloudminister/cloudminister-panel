# Generated by Django 4.0.6 on 2023-04-28 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_alter_country_id_alter_employeeprofile_id'),
        ('Project', '0036_remove_project_bid_and_more'),
        ('affiliaterouter', '0005_alter_affiliaterouterquestions_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='affiliaterouterquestionsdata',
            name='language',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='affiliate_router_question_data', to='Project.language'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='affiliaterouterquestionsdata',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='affiliate_router_question_data', to='employee.country'),
            preserve_default=False,
        ),
    ]
