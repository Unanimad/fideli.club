# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0009_auto_20170207_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='filled',
            field=models.BooleanField(default=0, verbose_name='Preenchido?'),
        ),
    ]
