# Generated by Django 5.1 on 2024-08-09 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0007_alter_eventregistration_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eventregistration",
            name="distance",
            field=models.CharField(
                choices=[(5, "5 km"), (10, "10 km"), (21, "21 km"), (42, "42 km")],
                max_length=10,
            ),
        ),
    ]
