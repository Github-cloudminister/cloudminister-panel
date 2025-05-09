# Generated by Django 5.0.6 on 2025-01-16 18:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bid', '0002_alter_bid_id_alter_bidrow_id'),
        ('Customer', '0006_customerorganization_threat_potential_score'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='bid_category',
            field=models.CharField(blank=True, choices=[('1', 'Automotive'), ('2', 'Beauty/Cosmetics'), ('3', 'Beverages - Alcoholic'), ('4', 'Beverages - Non Alcoholic'), ('5', 'Education'), ('6', 'Electronics/Computer/Software'), ('7', 'Entertainment (Movies, Music, TV, Etc)'), ('8', 'Fashion/Clothing'), ('9', 'Financial Services/Insurance'), ('10', 'Food/Snacks'), ('11', 'Gambling/Lottery'), ('12', 'Healthcare/Pharmaceuticals'), ('13', 'Home (Utilities/Appliances, ...)'), ('14', 'Home Entertainment (DVD,VHS)'), ('15', 'Home Improvement/Real Estate/Construction'), ('16', 'IT (Servers,Databases, Etc)'), ('17', 'Personal Care/Toiletries'), ('18', 'Pets'), ('19', 'Politics'), ('20', 'Publishing (Newspaper, Magazines, Books)'), ('21', 'Restaurants'), ('22', 'Sports/Outdoor'), ('23', 'Telecommunications (Phone, Cell Phone, Cable)'), ('24', 'Tobacco (Smokers)'), ('25', 'Toys'), ('26', 'Transportation/Shipping'), ('27', 'Travel'), ('28', 'Websites/Internet/E-Commerce'), ('29', 'other'), ('30', 'Sensitive Content'), ('31', 'Explicit Content'), ('32', 'Gaming'), ('33', 'HRDM'), ('34', 'Job/Career'), ('35', 'Shopping'), ('36', 'Parenting'), ('37', 'Religion'), ('38', 'ITDM'), ('39', 'Marketing/Advertising'), ('40', 'Other - B2B'), ('41', 'Ailment'), ('42', 'Social Media'), ('43', 'SBOs (Small Business Owners)'), ('44', 'Engineering'), ('45', 'Manufacturing'), ('46', 'Retail'), ('47', 'Opinion Elites'), ('48', 'Retail')], default='1', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='bid',
            name='bid_currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Customer.currency'),
        ),
        migrations.AddField(
            model_name='bid',
            name='secondary_project_manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bidrow',
            name='finalised_row_cpi',
            field=models.FloatField(default=0),
        ),
    ]
