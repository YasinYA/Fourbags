# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-31 03:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apparel', '0009_auto_20160830_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemimage',
            name='cloth_images',
        ),
        migrations.RemoveField(
            model_name='itemimage',
            name='shoes_images',
        ),
        migrations.AddField(
            model_name='cloth',
            name='item_image',
            field=models.URLField(default='Item Images', max_length=1500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shoe',
            name='item_image',
            field=models.URLField(default='Item Images', max_length=1500),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ItemImage',
        ),
    ]
