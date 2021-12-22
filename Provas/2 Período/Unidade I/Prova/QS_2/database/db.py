# importacoes
import pickle
from typing import Any

# funcao que cria o banco de dados pela primeira vez
def inicializar_PDB():
    with open('database/pessoa.pkl', 'wb') as file:
        pickle.dump([], file)

# funcao para registrar a pessoa no banco
def cadastrar_PDB(info: dict):
    with open('database/pessoa.pkl', 'rb') as file:
        arquivo_salvo = pickle.load(file)

    arquivo_salvo.append(info)
    print(arquivo_salvo)

    with open('database/pessoa.pkl', 'wb') as file:
        pickle.dump(arquivo_salvo, file)


# funcao que modifica o status das vagas
def mudarStatusVet_PDB(cpf):
   
    with open('database/pessoa.pkl', 'rb') as file:
        arquivo_salvo = pickle.load(file)

    compara_cpf = str(cpf)

    for pessoa in arquivo_salvo:
        if pessoa["CPF"] == compara_cpf:
            pessoa["STATUS"] = False

    with open('database/pessoa.pkl', 'wb') as file:
        pickle.dump(arquivo_salvo, file)


# funcao para tornar status TRUE de volta pra False
def dbFalse():
    with open('database/pessoa.pkl', 'rb') as file:
        arquivo_salvo = pickle.load(file)

    for pessoa in arquivo_salvo:
        # procura quem tem true, muda pra false e apaga os dados temporarios
        if pessoa["CANCELA"] == 'TRUE':
            pessoa["CANCELA"] = 'FALSE'
            del pessoa["FILEIRACANCELADA"]
            del pessoa["COLUNACANCELADA"]
            
    with open('database/pessoa.pkl', 'wb') as file:
        pickle.dump(arquivo_salvo, file)


# funcao que carrega o banco de dados
def carregar_PDB():
    with open('database/pessoa.pkl', 'rb') as file:
        return pickle.load(file)

# funcao que chega se o cpf ja existe no sistema
def checacpf_PDB(info, cpf):
    for pessoa in info:
        if pessoa["CPF"] == cpf:
            return True

    return None

# funcao que chega se o cfmv ja existe no sistema
def checacfmv_PDB(info, cfmv):
    for pessoa in info:
        if pessoa["CFMV"] == cfmv:
            return True

    return None

# funcao que busca os dados no banco e printa na tela
def consulta_PDB(info, cpf):
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
def consulta_ADB(info, code, data, valor, cfmv, status):
    with open('database/pet.pkl', 'rb') as file:
        arquivo_salvo = pickle.load(file)

    for animal in arquivo_salvo:
        if animal["CODIGO"] == code:
            animal["DATA"] = data
            animal["STATUS"] = status
            animal["VALOR"] = valor
            animal["CFMV"] = cfmv

    with open('database/pet.pkl', 'wb') as file:
        pickle.dump(arquivo_salvo, file)



# funcao que carrega o banco de dados
def carrega_ADB():
    with open('database/pet.pkl', 'rb') as file:
        return pickle.load(file)

# funcao que chega se o cpf ja existe no sistema
def checaCode_ADB(info, code):
    for animal in info:
        if animal["CODIGO"] == code:
            return True

    return None


def checaData_ADB(info, data):
    for animal in info:
        if animal["DATA"] == data:
            return True

    return None



