# Generated by Django 4.2.6 on 2023-11-01 03:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0004_palestrante_evento_anunciado_por_evento_palestrantes"),
    ]

    operations = [
        migrations.AddField(
            model_name="evento",
            name="decription",
            field=models.TextField(blank=True, null=True),
        ),
    ]
