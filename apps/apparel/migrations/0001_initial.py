# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-27 13:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cloth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_title', models.CharField(max_length=300)),
                ('item_brand', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('Men', 'Male'), ('Women', 'Female')], max_length=100)),
                ('item_price', models.IntegerField()),
                ('item_color', models.CharField(max_length=100)),
                ('is_in_stock', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('outerwear', 'OUTERWEAR'), ('socks', 'SOCKS'), ('shirts', 'SHIRTS'), ('t-shirts', 'T-SHIRTS'), ('polo', 'POLO'), ('shirts', 'SHIRTS'), ('underwear', 'UNDERWEAR'), ('pants', 'PANTS'), ('jeans', 'JEANS'), ('shorts', 'SHORTS'), ('ethnic', 'ETHNIC'), ('wear', 'WEAR'), ('beachwear', 'BEACHWEAR')], default='Category', max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(max_length=1000, upload_to='static/images/clothes')),
                ('item_images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemimage_images', to='apparel.Cloth')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sizes', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra-Large')], max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='cloth',
            name='sizes',
            field=models.ManyToManyField(related_name='cloth_sizes', to='apparel.Size'),
        ),
    ]
