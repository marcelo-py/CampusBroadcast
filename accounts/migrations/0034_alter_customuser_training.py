# Generated by Django 4.2.6 on 2023-11-21 18:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0033_atividadealunos_nome_projeto"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="training",
            field=models.CharField(
                blank=True, max_length=20, null=True, verbose_name="curso ou formação"
            ),
        ),
    ]
