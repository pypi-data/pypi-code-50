# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-31 20:15
from __future__ import unicode_literals

from django.db import migrations, models
import shuup.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shuup_testing', '0001_squashed_0003_update_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('separated_values', shuup.core.fields.SeparatedValuesField(blank=True)),
                ('separated_values_semi', shuup.core.fields.SeparatedValuesField(blank=True)),
                ('separated_values_dash', shuup.core.fields.SeparatedValuesField(blank=True)),
            ],
        ),
    ]
