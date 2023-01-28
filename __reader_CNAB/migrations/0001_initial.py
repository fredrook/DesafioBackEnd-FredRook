# Generated by Django 4.1.5 on 2023-01-27 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ArchiveCNAB",
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
                    "tipo",
                    models.CharField(
                        choices=[
                            (1, "Débito"),
                            (2, "Boleto"),
                            (3, "Financiamento"),
                            (4, "Crédito"),
                            (5, "Recebimento Empréstimo"),
                            (6, "Vendas"),
                            (7, "Recebimento TED"),
                            (8, "Recebimento DOC"),
                            (9, "Aluguel"),
                        ],
                        max_length=1000,
                    ),
                ),
                ("data", models.DateField()),
                ("valor", models.DecimalField(decimal_places=2, max_digits=10)),
                ("cpf", models.CharField(max_length=11)),
                ("cartao", models.CharField(max_length=12)),
                ("hora", models.TimeField()),
                ("dono", models.CharField(max_length=14)),
                ("nome", models.CharField(max_length=19)),
                ("loja", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="UploadFile",
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
                ("archive", models.FileField(upload_to="upload")),
            ],
        ),
    ]
