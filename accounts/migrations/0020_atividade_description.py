# Generated by Django 4.2.6 on 2023-11-08 02:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0019_remove_atividade_evento_atividade_data_rel_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="atividade",
            name="description",
            field=models.TextField(blank=True, max_length=120, null=True),
        ),
    ]
