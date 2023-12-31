# Generated by Django 4.2.6 on 2023-11-22 01:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Itens",
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
                    "nome_alimento",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Donate",
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
                ("nome", models.CharField(blank=True, max_length=500, null=True)),
                ("email", models.EmailField(blank=True, max_length=200, null=True)),
                ("telefone", models.CharField(blank=True, max_length=25, null=True)),
                (
                    "local",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("prefeitura", "prefeitura"),
                            ("igreja", "igreja"),
                            ("praca", "praça"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
                ("data", models.DateField(default=django.utils.timezone.now)),
                (
                    "itens",
                    models.ManyToManyField(
                        related_name="itens_doado", to="landingpage.itens"
                    ),
                ),
            ],
        ),
    ]
