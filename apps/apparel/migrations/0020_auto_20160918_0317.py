# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-18 03:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apparel', '0019_auto_20160917_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemimage',
            name='itemImage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='apparel.Item'),
        ),
    ]
