# Generated by Django 3.1.2 on 2020-10-05 21:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Status",
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
                (
                    "name",
                    models.CharField(max_length=30, unique=True, verbose_name="Cтатус"),
                ),
            ],
            options={"verbose_name": "Статус", "verbose_name_plural": "Статусы",},
        ),
        migrations.CreateModel(
            name="Task",
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
                ("name", models.CharField(max_length=30, verbose_name="Название")),
                (
                    "description",
                    models.TextField(max_length=250, verbose_name="Описание"),
                ),
                (
                    "creation_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "end_date",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        verbose_name="Планируемая дата завершения",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="tasks.status",
                        to_field="name",
                        verbose_name="Статус",
                    ),
                ),
            ],
            options={"verbose_name": "Задача", "verbose_name_plural": "Задачи",},
        ),
        migrations.CreateModel(
            name="HistoricalTask",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=30, verbose_name="Название")),
                (
                    "description",
                    models.TextField(max_length=250, verbose_name="Описание"),
                ),
                (
                    "creation_date",
                    models.DateTimeField(
                        blank=True, editable=False, verbose_name="Дата создания"
                    ),
                ),
                (
                    "end_date",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        verbose_name="Планируемая дата завершения",
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="tasks.status",
                        to_field="name",
                        verbose_name="Статус",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Задача",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
