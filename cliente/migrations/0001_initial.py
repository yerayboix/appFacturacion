# Generated by Django 4.2.6 on 2023-10-13 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cliente",
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
                ("nombre", models.CharField(default="", max_length=256)),
                ("domicilio", models.CharField(default="", max_length=256)),
                ("cp", models.IntegerField(blank=True, default=0, null=True)),
                ("ciudad", models.CharField(default="", max_length=256)),
                ("telefono", models.CharField(default="", max_length=256)),
                (
                    "tipo",
                    models.CharField(
                        choices=[("PAR", "Particular"), ("PRO", "Profesional")],
                        default="PAR",
                        max_length=3,
                    ),
                ),
                (
                    "nif",
                    models.CharField(blank=True, default="", max_length=256, null=True),
                ),
            ],
            options={
                "verbose_name": "Cliente",
                "verbose_name_plural": "Clientes",
                "ordering": ["pk"],
            },
        ),
    ]
