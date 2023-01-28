from .forms import UploadFileForm
from .models import UploadFile, ArchiveCNAB
from django.shortcuts import render
import ipdb


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        file = request.FILES["file"]

        CNAB_archive = UploadFile.objects.create(archive=file)

        CNAB_archive.save()

        transactions_tipes = []

        with open(
            f"./{str(CNAB_archive.archive)}", "r", encoding="utf-8"
        ) as archive_file:
            for archiveCNAB in archive_file:
                transactions_tipes.append(archiveCNAB)

        for loop_arc_cnab in transactions_tipes:
            tipo = loop_arc_cnab[:1]
            ano = loop_arc_cnab[1:5]
            mes = loop_arc_cnab[5:7]
            dia = loop_arc_cnab[7:9]
            valor = loop_arc_cnab[9:19]
            cpf: str = loop_arc_cnab[19:30]
            cartao: str = loop_arc_cnab[30:42]
            hora = loop_arc_cnab[42:44]
            minuto = loop_arc_cnab[44:46]
            segundo = loop_arc_cnab[46:48]
            dono: str = loop_arc_cnab[48:62]
            nome: str = loop_arc_cnab[62:81]
            loja = loop_arc_cnab[81:91]

            data = f"{ano}-{mes}-{dia}"
            valor = int(valor) / 100
            horario = f"{hora}:{minuto}:{segundo}"

            if tipo == "1":
                tipo = "Débito"

            elif tipo == "2":
                tipo = "Boleto"

            elif tipo == "3":
                tipo = "Financiamento"

            elif tipo == "4":
                tipo = "Crédito"

            elif tipo == "5":
                tipo = "Recebimento Empréstimo"

            elif tipo == "6":
                tipo = "Vendas"

            elif tipo == "7":
                tipo = "Recebimento TED"

            elif tipo == "8":
                tipo = "Recebimento DOC"

            elif tipo == "9":
                tipo = "Aluguel"

            reader = ArchiveCNAB.objects.create(
                tipo=tipo.strip(),
                data=data.strip(),
                valor=valor,
                cpf=cpf.strip(),
                cartao=cartao.strip(),
                hora=horario.strip(),
                dono=dono.strip(),
                nome=nome.strip(),
                loja=loja.strip(),
            )

            reader.save()

        transacoes = ArchiveCNAB.objects.values(
            "tipo", "valor", "data", "cpf", "cartao", "hora", "dono", "nome", "loja"
        ).order_by("dono")

        saldo_total_por_loja = {}

        for transacao in transacoes:
            if transacao["dono"] not in saldo_total_por_loja:
                saldo_total_por_loja[transacao["dono"]] = 0
            if (
                transacao["tipo"] == "Boleto"
                or transacao["tipo"] == "Financiamento"
                or transacao["tipo"] == "Aluguel"
            ):
                saldo_total_por_loja[transacao["dono"]] -= transacao["valor"]
            else:
                saldo_total_por_loja[transacao["dono"]] += transacao["valor"]

        return render(
            request,
            "renderResultsPage.html",
            context={
                "transacoes": transacoes,
                "saldo_total_por_loja": saldo_total_por_loja,
            },
        )

    else:
        form = UploadFileForm()
    return render(request, "upload.html", {"form": form})
