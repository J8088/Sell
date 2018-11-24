# Generated by Django 2.1.1 on 2018-11-17 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_auto_20181116_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_seo',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_code',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]