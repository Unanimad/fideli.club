# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0012_auto_20170210_0728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='status',
        ),
        migrations.AddField(
            model_name='company',
            name='token',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
    ]