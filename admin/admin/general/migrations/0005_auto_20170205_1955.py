# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-02-05 22:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0004_auto_20170205_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='converted',
            field=models.BooleanField(default=0, verbose_name='Convertido?'),
        ),
        migrations.AlterField(
            model_name='card',
            name='configuration',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.CardConfiguration', verbose_name='Configuração'),
        ),
        migrations.AlterField(
            model_name='card',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.Service', verbose_name='Serviço'),
        ),
    ]
