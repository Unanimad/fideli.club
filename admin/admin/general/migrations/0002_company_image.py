# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-02-05 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
