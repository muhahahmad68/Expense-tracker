# Generated by Django 5.0.6 on 2024-05-13 22:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="book",
            old_name="subtitles",
            new_name="subtitle",
        ),
    ]
