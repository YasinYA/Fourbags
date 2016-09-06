# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-06 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apparel', '0013_item_item_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='sizes',
            field=models.ManyToManyField(blank=True, related_name='shoe_size', to='apparel.Size'),
        ),
    ]
