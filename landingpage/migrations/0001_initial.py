# Generated by Django 5.0.1 on 2024-01-16 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LeadsForm",
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
                ("nome", models.CharField(max_length=100, verbose_name="Nome")),
                ("email", models.EmailField(max_length=200, verbose_name="E-mail")),
                ("phone", models.CharField(max_length=16, verbose_name="Celular")),
                (
                    "date_created",
                    models.DateField(auto_now=True, verbose_name="Data de cadastro"),
                ),
                (
                    "leadsource",
                    models.CharField(max_length=20, verbose_name="Origem cadastro"),
                ),
            ],
        ),
    ]