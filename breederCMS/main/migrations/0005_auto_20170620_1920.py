# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20170620_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animalentry',
            name='picture',
            field=models.ImageField(blank=True, upload_to='images/<django.db.models.fields.CharField>'),
        ),
    ]
