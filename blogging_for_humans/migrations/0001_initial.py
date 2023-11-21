# coding=utf-8
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Model01",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("model01_id", models.CharField(max_length=250)),
                ("field_01 ", models.CharField(max_length=255)),
            ],
        ),
    ]
