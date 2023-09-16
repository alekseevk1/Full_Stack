# Generated by Django 4.2.5 on 2023-09-14 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                (
                    "name",
                    models.CharField(
                        db_index=True, max_length=70, verbose_name="Категория"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(max_length=255, unique=True, verbose_name="URL"),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "db_table": "",
                "ordering": ["id"],
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Products",
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
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                (
                    "slug",
                    models.SlugField(max_length=255, unique=True, verbose_name="URL"),
                ),
                (
                    "photo",
                    models.ImageField(
                        upload_to="photos/%Y/%m/%d", verbose_name="Фотография"
                    ),
                ),
                ("is_Ready", models.BooleanField(default=True)),
                ("price", models.IntegerField(verbose_name="Цена")),
                ("amount", models.IntegerField(verbose_name="Количество")),
                (
                    "time_create",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время создания"
                    ),
                ),
                (
                    "time_update",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Время обновления"
                    ),
                ),
                ("description", models.TextField(blank=True, verbose_name="Описание")),
                ("action", models.BooleanField(default=False, verbose_name="Акция")),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="products.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Товары",
                "verbose_name_plural": "Товары",
                "db_table": "",
                "ordering": ["time_create", "title"],
                "managed": True,
            },
        ),
    ]