# Generated by Django 4.2.6 on 2023-11-01 03:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0005_evento_decription"),
    ]

    operations = [
        migrations.AlterField(
            model_name="evento",
            name="anunciado_por",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]