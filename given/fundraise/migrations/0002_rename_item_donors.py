# Generated by Django 5.2.3 on 2025-06-22 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("fundraise", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Item",
            new_name="donors",
        ),
    ]
