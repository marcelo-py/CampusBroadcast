# Generated by Django 4.2.6 on 2023-11-03 20:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0009_alter_palestrante_training"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="training",
            field=models.CharField(
                blank=True, max_length=20, null=True, verbose_name="formação"
            ),
        ),
    ]