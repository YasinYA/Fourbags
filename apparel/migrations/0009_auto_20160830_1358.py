# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-30 13:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apparel', '0008_auto_20160830_1357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_title', models.CharField(max_length=300)),
                ('item_brand', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('Men', 'Male'), ('Women', 'Female')], max_length=100)),
                ('item_price', models.FloatField()),
                ('item_color', models.CharField(max_length=100)),
                ('is_in_stock', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(choices=[('SLIP-ONS', 'SLIP-ONS'), ('HIGH TOPS', 'HIGH TOPS'), ('LOW TOPS', 'LOW TOPS'), ('SANDALS & FLIP FLOPS', 'SANDALS & FLIP FLOPS'), ('SNEAKERS & PLIMSOLLS', 'SNEAKERS & PLIMSOLLS'), ('FORMAL', 'FORMAL'), ('SPORTS', 'SPORTS'), ('BOOTS', 'BOOTS'), ('BROGUES & DERBIES', 'BROGUES & DERBIES')], default='Category', max_length=200)),
                ('sizes', models.ManyToManyField(related_name='shoe_size', to='apparel.Size')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='shoes',
            name='sizes',
        ),
        migrations.AlterField(
            model_name='itemimage',
            name='shoes_images',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoes_images', to='apparel.Shoe'),
        ),
        migrations.DeleteModel(
            name='Shoes',
        ),
    ]
