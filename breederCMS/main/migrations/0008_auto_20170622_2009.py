# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20170621_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animalentry',
            name='cropping',
        ),
        migrations.AddField(
            model_name='animalentry',
            name='cropped_picture',
            field=models.ImageField(blank=True, upload_to='media/cropped/'),
        ),
    ]
