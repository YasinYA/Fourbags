# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-05 08:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('apparel', '0023_auto_20161027_0937'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='email',
        ),
        migrations.RemoveField(
            model_name='order',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone',
        ),
        migrations.AddField(
            model_name='order',
            name='is_new_buyer',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='order',
            name='when',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 11, 5, 8, 45, 28, 465149, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='buyer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='purchaser', to='apparel.Customer'),
            preserve_default=False,
        ),
    ]
