# Generated by Django 4.2 on 2024-02-16 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='facebook',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='Facebook Profile Url'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='agents/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Whatsapp Number'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='x',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='X Profile Url'),
        ),
    ]
