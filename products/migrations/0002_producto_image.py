# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='image',
            field=models.ImageField(blank=True, upload_to=b''),
        ),
    ]
