# Generated by Django 4.2.6 on 2023-11-04 15:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0015_atividade_delete_atividadeparaevento_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="atividade",
            name="membros",
            field=models.ManyToManyField(
                related_name="membros_evento", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
