# Generated by Django 4.2.2 on 2023-09-12 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tapa", "0013_alter_day_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="day",
            name="tap",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="tapa.tap"
            ),
        ),
    ]
