# Generated by Django 2.2.5 on 2021-04-13 07:01

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210413_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, null=True, size=None),
        ),
    ]
