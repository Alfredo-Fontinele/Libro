# Generated by Django 4.1.7 on 2023-03-08 18:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("author", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=250)),
            ],
        ),
    ]
