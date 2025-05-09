# Generated by Django 3.1.1 on 2021-02-10 17:34

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee', '0001_initial'),
        ('Customer', '0001_initial'),
        ('Supplier', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(max_length=3)),
                ('language_name', models.CharField(max_length=80)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='language_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='language_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-modified_at',),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200)),
                ('project_number', models.CharField(max_length=100)),
                ('project_category', models.CharField(choices=[('1', 'Automotive'), ('2', 'Beauty/Cosmetics'), ('3', 'Beverages - Alcoholic'), ('4', 'Beverages - Non Alcoholic'), ('5', 'Education'), ('6', 'Electronics/Computer/Software'), ('7', 'Entertainment (Movies, Music, TV, Etc)'), ('8', 'Fashion/Clothing'), ('9', 'Financial Services/Insurance'), ('10', 'Food/Snacks'), ('11', 'Gambling/Lottery'), ('12', 'Healthcare/Pharmaceuticals'), ('13', 'Home (Utilities/Appliances, ...)'), ('14', 'Home Entertainment (DVD,VHS)'), ('15', 'Home Improvement/Real Estate/Construction'), ('16', 'IT (Servers,Databases, Etc)'), ('17', 'Personal Care/Toiletries'), ('18', 'Pets'), ('19', 'Politics'), ('20', 'Publishing (Newspaper, Magazines, Books)'), ('21', 'Restaurants'), ('22', 'Sports/Outdoor'), ('23', 'Telecommunications (Phone, Cell Phone, Cable)'), ('24', 'Tobacco (Smokers)'), ('25', 'Toys'), ('26', 'Transportation/Shipping'), ('27', 'Travel'), ('28', 'Websites/Internet/E-Commerce'), ('29', 'other'), ('30', 'Sensitive Content'), ('31', 'Explicit Content'), ('32', 'Gaming'), ('33', 'HRDM'), ('34', 'Job/Career'), ('35', 'Shopping'), ('36', 'Parenting'), ('37', 'Religion'), ('38', 'ITDM'), ('39', 'Marketing/Advertising'), ('40', 'Other - B2B'), ('41', 'Ailment'), ('42', 'Social Media'), ('43', 'SBOs (Small Business Owners)'), ('44', 'Engineering'), ('45', 'Manufacturing'), ('46', 'Retail'), ('47', 'Opinion Elites'), ('48', 'Retail')], default='1', max_length=2)),
                ('project_device_type', models.CharField(choices=[('1', 'All'), ('2', 'Desktop/Laptop Only'), ('3', 'Tablet Only'), ('4', 'Mobile Only'), ('5', 'Dekstop + Tablet'), ('6', 'Dekstop + Mobile'), ('7', 'Tablet + Mobile')], default='2', max_length=1)),
                ('project_type', models.CharField(choices=[('1', 'Adhoc'), ('2', 'Tracker'), ('3', 'IHUT'), ('4', 'Community Recruit'), ('5', 'Panel Sourcing'), ('6', 'Qual'), ('7', 'IR Check'), ('8', 'Other')], default='5', max_length=1)),
                ('project_status', models.CharField(choices=[('Cancel', 'Cancel'), ('Booked', 'Booked'), ('Live', 'Live'), ('Paused', 'Paused'), ('Closed', 'Closed'), ('Reconciled', 'Reconciled'), ('Invoiced', 'Invoiced'), ('Archived', 'Archived')], default='Live', max_length=10)),
                ('project_redirectID', models.CharField(max_length=100)),
                ('project_revenue_month', models.CharField(choices=[('1', 'January'), ('2', 'February'), ('3', 'March'), ('4', 'April'), ('5', 'May'), ('6', 'June'), ('7', 'July'), ('8', 'August'), ('9', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')], default=2, max_length=2)),
                ('project_revenue_year', models.IntegerField(default=2021)),
                ('project_total_revenue', models.BigIntegerField(default=0)),
                ('project_notes', models.TextField()),
                ('project_redirect_type', models.CharField(choices=[('0', 'Static'), ('1', 'Dynamic')], default='1', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_modified_by', to=settings.AUTH_USER_MODEL)),
                ('project_client_contact_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_contact_person', to='Customer.clientcontact')),
                ('project_client_invoicing_contact_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoicing_contact_person', to='Customer.clientcontact')),
                ('project_country', models.ManyToManyField(to='employee.Country')),
                ('project_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.currency')),
                ('project_customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.customerorganization')),
                ('project_language', models.ManyToManyField(to='Project.Language')),
                ('project_manager', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='project_manager', to=settings.AUTH_USER_MODEL)),
                ('project_sales_person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='project_sales_person', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='ProjectGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_group_number', models.CharField(blank=True, max_length=7)),
                ('project_group_name', models.CharField(max_length=100)),
                ('project_audience_type', models.CharField(choices=[('1', 'B2B'), ('2', 'Consumer'), ('3', 'Healthcare'), ('4', 'Other')], default='1', max_length=1)),
                ('project_group_status', models.CharField(choices=[('Cancel', 'Cancel'), ('Booked', 'Booked'), ('Live', 'Live'), ('Paused', 'Paused'), ('Closed', 'Closed'), ('Reconciled', 'Reconciled'), ('Invoiced', 'Invoiced'), ('Archived', 'Archived')], default='Live', max_length=10)),
                ('project_group_encodedS_value', models.CharField(max_length=100)),
                ('project_group_encodedR_value', models.CharField(max_length=100)),
                ('project_group_redirectID', models.CharField(max_length=100)),
                ('project_group_liveurl', models.URLField(default='', null=True)),
                ('project_group_testurl', models.URLField(default='', null=True)),
                ('project_group_surveyurl', models.URLField()),
                ('project_group_client_url_type', models.CharField(choices=[('1', 'Single'), ('2', 'Multiple')], default='1', max_length=10)),
                ('project_group_incidence', models.IntegerField(default=100, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('project_group_loi', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(1)])),
                ('project_group_completes', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('project_group_clicks', models.IntegerField(default=0)),
                ('project_group_cpi', models.FloatField(default=0)),
                ('project_group_revenue', models.IntegerField(default=0)),
                ('project_group_startdate', models.DateField(default='')),
                ('project_group_enddate', models.DateField(default='')),
                ('project_group_security_check', models.BooleanField(default=False)),
                ('project_group_ip_check', models.BooleanField(default=False)),
                ('project_group_pid_check', models.BooleanField(default=False)),
                ('project_group_allowed_svscore', models.IntegerField(default=0)),
                ('project_group_allowed_dupescore', models.IntegerField(default=0)),
                ('project_group_allowed_fraudscore', models.IntegerField(default=0)),
                ('enable_panel', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_modified_by', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_project', to='Project.project')),
                ('project_group_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_country', to='employee.country')),
                ('project_group_language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_language', to='Project.language')),
            ],
            options={
                'ordering': ('-modified_at',),
            },
        ),
        migrations.CreateModel(
            name='ZipCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.CharField(max_length=20)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('project_group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project.projectgroup')),
                ('uploaded_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='zip_code_uploadby', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectLogTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actual_url', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='ProjectGroupSupplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completes', models.BigIntegerField(default=0)),
                ('clicks', models.IntegerField(default=0)),
                ('cpi', models.FloatField(default=0)),
                ('supplier_completeurl', models.URLField()),
                ('supplier_terminateurl', models.URLField()),
                ('supplier_quotafullurl', models.URLField()),
                ('supplier_securityterminateurl', models.URLField()),
                ('supplier_survey_url', models.URLField()),
                ('supplier_status', models.CharField(choices=[('Cancel', 'Cancel'), ('Booked', 'Booked'), ('Live', 'Live'), ('Paused', 'Paused'), ('Closed', 'Closed'), ('Reconciled', 'Reconciled'), ('Invoiced', 'Invoiced'), ('Archived', 'Archived')], default='Live', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='progrpsupp_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='progrpsupp_modified_by', to=settings.AUTH_USER_MODEL)),
                ('project_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_group', to='Project.projectgroup')),
                ('supplier_org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_orga', to='Supplier.supplierorganisation')),
            ],
            options={
                'ordering': ('-modified_at',),
            },
        ),
        migrations.CreateModel(
            name='ProjectGroupLogTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actual_url', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='MultipleURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_url', models.URLField()),
                ('client_url_id', models.CharField(default='', max_length=255, null=True)),
                ('is_used', models.BooleanField(default=False)),
                ('project_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project.projectgroup')),
            ],
            options={
                'ordering': ('is_used', 'id'),
            },
        ),
    ]
