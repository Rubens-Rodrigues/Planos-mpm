# Generated by Django 5.0.1 on 2024-01-24 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("landingpage", "0003_alter_leadsform_email_alter_leadsform_phone"),
    ]

    operations = [
        migrations.CreateModel(
            name="PreInscricao",
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
                ("nome", models.CharField(max_length=50)),
                ("telefone", models.CharField(max_length=14)),
            ],
        ),
    ]
