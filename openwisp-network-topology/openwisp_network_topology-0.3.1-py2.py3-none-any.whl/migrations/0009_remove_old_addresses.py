# Generated by Django 2.2.9 on 2020-01-3 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topology', '0008_migrate_addresses_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='addresses_old',
        ),
    ]
