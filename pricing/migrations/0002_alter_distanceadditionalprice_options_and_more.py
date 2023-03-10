# Generated by Django 4.1.5 on 2023-02-03 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pricing", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="distanceadditionalprice", options={"ordering": ("is_active",)},
        ),
        migrations.AlterModelOptions(
            name="distancebasepricing", options={"ordering": ("up_to_distance",)},
        ),
        migrations.AlterModelOptions(
            name="timemultiplierfactor", options={"ordering": ("up_to_time",)},
        ),
        migrations.AlterField(
            model_name="distanceadditionalprice",
            name="price",
            field=models.FloatField(default=0, help_text="In Rupees"),
        ),
    ]
