# Generated by Django 5.0.6 on 2025-01-16 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supplier', '0024_delete_supplierbuyerapimodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsupplierorganisation',
            name='sub_supplier_completeurl',
            field=models.URLField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='subsupplierorganisation',
            name='sub_supplier_internal_terminate_redirect_url',
            field=models.URLField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='subsupplierorganisation',
            name='sub_supplier_postbackurl',
            field=models.URLField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='subsupplierorganisation',
            name='sub_supplier_quotafullurl',
            field=models.URLField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='subsupplierorganisation',
            name='sub_supplier_routerurl',
            field=models.URLField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='subsupplierorganisation',
            name='sub_supplier_securityterminateurl',
            field=models.URLField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='subsupplierorganisation',
            name='sub_supplier_terminate_no_project_available',
            field=models.URLField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='subsupplierorganisation',
            name='sub_supplier_terminateurl',
            field=models.URLField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='supplierorganisation',
            name='supplier_completeurl',
            field=models.URLField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='supplierorganisation',
            name='supplier_internal_terminate_redirect_url',
            field=models.URLField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='supplierorganisation',
            name='supplier_postbackurl',
            field=models.URLField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='supplierorganisation',
            name='supplier_quotafullurl',
            field=models.URLField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='supplierorganisation',
            name='supplier_routerurl',
            field=models.URLField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='supplierorganisation',
            name='supplier_securityterminateurl',
            field=models.URLField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='supplierorganisation',
            name='supplier_terminate_no_project_available',
            field=models.URLField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='supplierorganisation',
            name='supplier_terminateurl',
            field=models.URLField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='supplierorgauthkeydetails',
            name='production_base_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='supplierorgauthkeydetails',
            name='staging_base_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
