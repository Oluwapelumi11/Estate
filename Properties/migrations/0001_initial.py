# Generated by Django 5.0 on 2024-02-16 09:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('type', models.CharField(choices=[('LIVING HOUSE', 'Living House'), ('HOUSE VILLA', 'House Villa'), ('HOUSE APARTMENT', 'House Apartment'), ('OFFICE FLOOR', 'Office Floor')], default='LIVING HOUSE', max_length=20, verbose_name='Property Type')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Price')),
                ('street', models.CharField(max_length=100, verbose_name='Street Address')),
                ('city', models.CharField(max_length=30, verbose_name='City')),
                ('zip_code', models.CharField(max_length=15, verbose_name='Zip Code')),
                ('status', models.CharField(max_length=30, verbose_name='Status')),
                ('date_listed', models.DateField(auto_now_add=True, verbose_name='Listing Data')),
                ('plot_size', models.IntegerField(verbose_name='Plot Size')),
                ('roof_type', models.CharField(max_length=50, verbose_name='Roof Type')),
                ('construction_company', models.CharField(max_length=50, verbose_name='Construction Company')),
                ('cooling', models.CharField(max_length=50, verbose_name='Cooling')),
                ('interior_size', models.CharField(max_length=50, verbose_name='Interior Size')),
                ('bedroom', models.IntegerField(verbose_name='Bedroom')),
                ('bedroom_size', models.CharField(max_length=50, verbose_name='Bedroom Size')),
                ('bathroom', models.IntegerField(verbose_name='Bathroom')),
                ('bathroom_size', models.CharField(max_length=50, verbose_name='Bathroom Size')),
                ('garage', models.IntegerField(verbose_name='Garage Capacity')),
                ('laundry_room_equipment', models.CharField(max_length=50, verbose_name='Laundry Equipments')),
                ('living_room_size', models.CharField(max_length=50, verbose_name='Living Room Size')),
                ('kitchen', models.CharField(max_length=50, verbose_name='Kitchen Size')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agents.agent')),
            ],
        ),
    ]
