# Generated by Django 4.1.6 on 2023-04-04 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipegenerator", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="RestrictionPreset",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
            ],
            options={"verbose_name_plural": "RestrictionPresets",},
        ),
        migrations.CreateModel(
            name="RestrictionPresetIngredient",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("presetid", models.IntegerField()),
                ("ingredientId", models.IntegerField()),
            ],
            options={"verbose_name_plural": "RestrictionPresetIngredients",},
        ),
        migrations.CreateModel(
            name="SelectedRestrictionPreset",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("presetid", models.IntegerField()),
                ("userName", models.CharField(max_length=255)),
            ],
            options={"verbose_name_plural": "SelectedRestrictionPresets",},
        ),
    ]