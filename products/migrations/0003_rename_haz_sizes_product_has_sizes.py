# Generated by Django 3.2.20 on 2023-08-15 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20230815_1245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='haz_sizes',
            new_name='has_sizes',
        ),
    ]
