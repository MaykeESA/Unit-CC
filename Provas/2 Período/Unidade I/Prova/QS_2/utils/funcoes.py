# Importacoes
import re
from database import db
from datetime import datetime


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


def valida_data(data):
    try:
        data_validada = datetime.strptime(data, '%d/%m/%Y').strftime('%d/%m/%Y')
        data_validada = str(data_validada)
        data_validada = data_validada
        return data_validada
    except ValueError:
        return False


def menu10():
    print(db.carregar_PDB())
    print(db.carrega_ADB())


