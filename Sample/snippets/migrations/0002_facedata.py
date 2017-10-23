# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaceData',
            fields=[
                ('identity', models.IntegerField()),
                ('rep', models.TextField()),
                ('phash', models.TextField(primary_key=True, serialize=False)),
                ('image', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/')),
            ],
        ),
    ]
