# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-28 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='item_number',
            field=models.CharField(default=0, max_length=4),
            preserve_default=False,
        ),
    ]
