# importacoes
import pickle
from typing import Any

# funcao que cria o banco de dados pela primeira vez
def inicializarDB():
    with open('database/data.pkl', 'wb') as file:
        pickle.dump([], file)

# funcao para registrar a pessoa no banco
def cadastrarDB(info: dict):
    with open('database/data.pkl', 'rb') as file:
        arquivo_salvo = pickle.load(file)

    arquivo_salvo.append(info)

    with open('database/data.pkl', 'wb') as file:
        pickle.dump(arquivo_salvo, file)


# funcao que modifica o status das vagas
def mudarstatus_vetDB(info, cpf):
    with open('database/data.pkl', 'rb') as file:
        arquivo_salvo = pickle.load(file)

    compara_cpf = str(info)

    for pessoa in arquivo_salvo:
        if pessoa["CPF"] == compara_cpf:
            pessoa["STATUS"] = False

    with open('database/data.pkl', 'wb') as file:
        pickle.dump(arquivo_salvo, file)


# funcao para tornar status TRUE de volta pra False
def dbFalse():
    with open('database/data.pkl', 'rb') as file:
        arquivo_salvo = pickle.load(file)

    for pessoa in arquivo_salvo:
        # procura quem tem true, muda pra false e apaga os dados temporarios
        if pessoa["CANCELA"] == 'TRUE':
            pessoa["CANCELA"] = 'FALSE'
            del pessoa["FILEIRACANCELADA"]
            del pessoa["COLUNACANCELADA"]
            
    with open('database/data.pkl', 'wb') as file:
        pickle.dump(arquivo_salvo, file)


# funcao que carrega o banco de dados
def carregarDB():
    with open('database/data.pkl', 'rb') as file:
        return pickle.load(file)

# funcao que chega se o cpf ja existe no sistema
def checacpfDB(info, cpf):
    for pessoa in info:
        if pessoa["CPF"] == cpf:
            return True

    return None

# funcao que chega se o cfmv ja existe no sistema
def checacfmvDB(info, cfmv):
    for pessoa in info:
        if pessoa["CFMV"] == cfmv:
            return True

    return None

# funcao que busca os dados no banco e printa na tela
def consultaDB(info, cpf):
    for pessoa in info:
        if pessoa["CPF"] == cpf:
            print("-=" * 8)
            print(f'Nome: {pessoa["NOME"]}')
            print(f'CPF: {pessoa["CPF"]}')
            if pessoa["FILEIRA"]:
                print(f'Vaga: {pessoa["FILEIRA"]} {pessoa["COLUNA"]}')
            else:
                print(f'Vaga: Sem Reserva')
            print("-=" * 8)
        else:
            continue
    return



# funcao que cria o banco de dados pela primeira vez
def inicializar_ADB():
    with open('database/pet.pkl', 'wb') as file:
        pickle.dump([], file)


# funcao para registrar a pessoa no banco
def cadastrar_ADB(info: dict):
    with open('database/pet.pkl', 'rb') as file:
        arquivo_salvo = pickle.load(file)

    arquivo_salvo.append(info)

    with open('database/pet.pkl', 'wb') as file:
        pickle.dump(arquivo_salvo, file)


# funcao que modifica o status das vagas
def consulta_ADB(info, code, data, valor, status):
    with open('database/pet.pkl', 'rb') as file:
        arquivo_salvo = pickle.load(file)

    for animal in arquivo_salvo:
        if animal["CODE"] == code:
            animal["DATA"] = data
            animal["STATUS"] = status
            animal["VALOR"] = valor

    with open('database/pet.pkl', 'wb') as file:
        pickle.dump(arquivo_salvo, file)



# funcao que carrega o banco de dados
def carrega_ADB():
    with open('database/pet.pkl', 'rb') as file:
        return pickle.load(file)

# funcao que chega se o cpf ja existe no sistema
def checacode_ADB(info, code):
    for animal in info:
        if animal["CODE"] == code:
            return True

    return None


def checadata_ADB(info, data):
    for animal in info:
        if animal["DATA"] == data:
            return True

    return None



