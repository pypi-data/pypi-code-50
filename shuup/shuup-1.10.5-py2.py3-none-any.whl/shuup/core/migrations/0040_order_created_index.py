# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-12-14 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuup', '0039_alter_names'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created on'),
        ),
    ]
