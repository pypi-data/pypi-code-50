# Generated by Django 2.1.2 on 2019-02-15 00:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('list_based_flavorpack', '0003_auto_20190123_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listbasedregion',
            name='file_id',
            field=models.UUIDField(default=uuid.uuid1),
        ),
    ]
