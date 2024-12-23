# Generated by Django 5.1.3 on 2024-12-01 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=20)),
                (
                    "cover",
                    models.CharField(
                        choices=[
                            ("cover1", "/book_covers/cover_white.png"),
                            ("cover2", "/book_covers/cover_white.png"),
                            ("cover3", "/book_covers/cover_white.png"),
                            ("cover4", "/book_covers/cover_white.png"),
                            ("cover5", "/book_covers/cover_white.png"),
                        ],
                        default="cover1",
                        max_length=20,
                    ),
                ),
                ("simple_explanation", models.CharField(max_length=50)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="BookCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
    ]
