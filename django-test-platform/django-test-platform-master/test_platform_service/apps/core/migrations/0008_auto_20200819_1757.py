# Generated by Django 3.1 on 2020-08-19 17:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_test_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='date_created',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата создания'),
        ),
    ]
