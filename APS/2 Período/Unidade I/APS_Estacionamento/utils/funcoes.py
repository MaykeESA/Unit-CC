# Importacoes
import re
from database import db
import os

# funcao para checar se o cpf esta em formato correto
def valida_cpf(cpf, formata=False):
    # transfoma 11111111111 em 111.111.111-11 (nao usado)
    if formata:
        cpf = re.sub("(\d{3})(\d{3})(\d{3})(\d{2})", "\\1.\\2.\\3-\\4", cpf)
        return cpf

    if not formata:
        cpf = str(cpf)
        cpf = re.sub(r'[^0-9]', '', cpf)

        if not cpf or len(cpf) != 11:
            return 'None'
        else:
            return cpf

# funcao que cria a matriz do estacionamento
def matriz():
    estacionamento = []
    for i in range(1, 7):
        linha = []
        for j in range(1, 11):
            linha.append('X')
        estacionamento.append(linha)
    return estacionamento

def menu128():
        print("\n")
        print(db.carregarDB())
        print(db.carregarMDB())
        print("\n")


def menu5():
    if os.path.exists("relatorios/reserva.txt"):
        print("Relatorio de Reservas feito (checar a pasta relatorios)\n")
    else:
        print("Nenhuma reserva foi feita ainda")


def menu6():
    if os.path.exists("relatorios/vagalivre.txt"):
        print("Relatorio de Vagas Livres feito (checar a pasta relatorios)\n")
    else:
        print("Nenhuma vaga foi registrada ainda")


def menu7():
    if os.path.exists("relatorios/cancelamentoreserva.txt"):
        print("Relatorio de Cancelamento de Reservas feito (checar a pasta relatorios)\n")
    else:
        print("Nenhum cancelamento foi feita ainda")



