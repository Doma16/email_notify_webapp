# Generated by Django 4.2.2 on 2023-09-09 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tapa", "0003_day_tap_send_days"),
    ]

    operations = [
        migrations.RenameField(
            model_name="day",
            old_name="date",
            new_name="time",
        ),
        migrations.AlterField(
            model_name="tap",
            name="send_days",
            field=models.ManyToManyField(blank=True, to="tapa.day"),
        ),
    ]
