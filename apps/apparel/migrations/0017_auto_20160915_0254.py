# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-15 02:54
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('apparel', '0016_auto_20160915_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemimage',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to='media'),
        ),
    ]
