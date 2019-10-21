# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 20:39
from __future__ import unicode_literals

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20170621_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animalentry',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('picture', '50x50', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]