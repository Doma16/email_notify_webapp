# Generated by Django 4.2.2 on 2023-09-10 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tapa", "0012_alter_tap_send_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="day",
            name="time",
            field=models.TimeField(blank=True, null=True),
        ),
    ]
