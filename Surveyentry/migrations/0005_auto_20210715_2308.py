# Generated by Django 3.1.1 on 2021-07-15 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Supplier', '0003_auto_20210715_2303'),
        ('Project', '0006_auto_20210715_2308'),
        ('Surveyentry', '0004_respondentreconcilation_supplier_verified_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respondentreconcilation',
            name='supplier_verified_id',
        ),
        migrations.AddField(
            model_name='respondentdetail',
            name='supplier_id_rejected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='respondentsupplierdetail',
            name='supplier_postback_url',
            field=models.URLField(default='', null=True),
        ),
        migrations.AddField(
            model_name='respondentsupplierdetail',
            name='supplier_postback_url_response',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='respondentsupplierdetail',
            name='supplier_complete_url',
            field=models.URLField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='respondentsupplierdetail',
            name='supplier_quotafull_url',
            field=models.URLField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='respondentsupplierdetail',
            name='supplier_securityterminate_url',
            field=models.URLField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='respondentsupplierdetail',
            name='supplier_terminate_url',
            field=models.URLField(default='', null=True),
        ),
        migrations.CreateModel(
            name='RespondentDetailsRelationalfield',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Project.project')),
                ('project_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Project.projectgroup')),
                ('respondent', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Surveyentry.respondentdetail')),
                ('source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Supplier.supplierorganisation')),
            ],
        ),
        migrations.CreateModel(
            name='DisqoQueryParam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('clientId', models.IntegerField(default=0)),
                ('pid', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('projectId', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('quotaIds', models.TextField(blank=True, default='', null=True)),
                ('supplierId', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('tid', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('respondent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Surveyentry.respondentdetail')),
            ],
        ),
    ]
