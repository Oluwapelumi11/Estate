# Generated by Django 5.0 on 2024-02-16 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('email', models.CharField(max_length=200, verbose_name='Email')),
                ('phone', models.IntegerField(verbose_name='Phone')),
                ('image', models.ImageField(upload_to='agents/', verbose_name='Image')),
                ('facebook', models.URLField(max_length=255, verbose_name='Facebook Profile Url')),
                ('x', models.URLField(max_length=255, verbose_name='X Profile Url')),
                ('whatsapp', models.CharField(max_length=255, verbose_name='Whatsapp Number')),
            ],
        ),
    ]
