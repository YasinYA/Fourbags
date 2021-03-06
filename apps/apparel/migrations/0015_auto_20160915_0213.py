# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-15 02:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apparel', '0014_auto_20160906_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='item_image',
        ),
        migrations.AddField(
            model_name='itemimage',
            name='item_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apparel.Item'),
        ),
    ]
