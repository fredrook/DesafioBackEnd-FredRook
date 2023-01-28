from django.db import models


class UploadFile(models.Model):
    archive = models.FileField(upload_to="upload")


class ArchiveCNAB(models.Model):
    TIPO_CHOICES = (
        (1, "Débito"),
        (2, "Boleto"),
        (3, "Financiamento"),
        (4, "Crédito"),
        (5, "Recebimento Empréstimo"),
        (6, "Vendas"),
        (7, "Recebimento TED"),
        (8, "Recebimento DOC"),
        (9, "Aluguel"),
    )

    tipo = models.CharField(max_length=1000, choices=TIPO_CHOICES)
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    hora = models.TimeField()
    dono = models.CharField(max_length=14)
    nome = models.CharField(max_length=19)
    loja = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} - {self.get_tipo_display()} - R$ {self.valor}"
