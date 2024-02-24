# Generated by Django 5.0 on 2024-02-24 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Properties', '0003_property_description_property_featured_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='type',
        ),
        migrations.AddField(
            model_name='property',
            name='property_category',
            field=models.CharField(blank=True, choices=[('LIVING HOUSE', 'Living House'), ('HOUSE VILLA', 'House Villa'), ('HOUSE APARTMENT', 'House Apartment'), ('OFFICE FLOOR', 'Office Floor')], default='LIVING HOUSE', max_length=20, null=True, verbose_name='Property Category'),
        ),
        migrations.AddField(
            model_name='property',
            name='property_type',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Property Type'),
        ),
    ]
