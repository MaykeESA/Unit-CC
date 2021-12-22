# importacoes
import pickle
from utils.funcoes import matriz
import log
from utils import messages as msg

# funcao que cria o banco de dados pela primeira vez
def inicializarDB():
    with open('database/data.pkl', 'wb') as file:
        pickle.dump([], file)
    log.LogGeral(msg.success_db_iniciar)

# funcao para registrar a pessoa no banco
def cadastrarDB(info: dict):
    with open('database/data.pkl', 'rb') as file:
        arquivo_salvo = pickle.load(file)

    arquivo_salvo.append(info)

    with open('database/data.pkl', 'wb') as file:
        pickle.dump(arquivo_salvo, file)


# funcao que modifica o status das vagas
def modificarDB(info, fileira, coluna, coluninha=None, fileirinha=None, cancela=False):
    with open('database/data.pkl', 'rb') as file:
        arquivo_salvo = pickle.load(file)

    compara_cpf = str(info)

    for pessoa in arquivo_salvo:
        # se a pessoa estiver reservando, atualizar as vagas
        if pessoa["CPF"] == compara_cpf:
            pessoa["COLUNA"] = coluna
            pessoa["FILEIRA"] = fileira
            pessoa["CANCELA"] = 'FALSE'
        if pessoa["CPF"] == compara_cpf:
            # se a pessoa estiver cancelando, apagar os dados das vagas fazer copia dos dados para mostrar no relatorio depois
            if cancela:
                pessoa['CANCELA'] = 'TRUE'
                pessoa["FILEIRACANCELADA"] = fileirinha
                pessoa["COLUNACANCELADA"] = coluninha
        
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
    log.LogGeral(msg.info_db_carregar)
    with open('database/data.pkl', 'rb') as file:
        return pickle.load(file)

# funcao que chega se o cpf esta registrado no banco de dados
def checaDB(info, cpf):
    for pessoa in info:
        if pessoa["CPF"] == cpf:
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


# funcao que cria o banco de dados da matriz pela primeira vez
def inicializarMDB():
    estacionamento_main = matriz()
    with open('database/matriz.pkl', 'wb') as file:
        pickle.dump(estacionamento_main, file)
    log.LogGeral(msg.success_mdb_iniciar)

# funcao que atualiza a matriz
def cadastrarMDB(info):
    with open('database/matriz.pkl', 'wb') as file:
        pickle.dump(info, file)

# funcao que carrega o banco da matriz
def carregarMDB():
    log.LogGeral(msg.info_mdb_carregar)
    with open('database/matriz.pkl', 'rb') as file:
        return pickle.load(file)


