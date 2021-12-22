# importacoes
from time import sleep
import log
import copy
from database import db
from utils import funcoes
from utils import messages as msg

# mold do dicionario por pessoa
dic_dados = {
    'NOME': '',
    'CPF': '',
    'COLUNA': '',
    'FILEIRA': '',
    'CANCELA': 'FALSE',
}

# funcao do cadastro de pessoa
def cadastro():
    nome = input("Digite seu nome: ")
    log.LogGeral(msg.info_nome, nome)

    # verificar se o cpf e valido
    cpf = input("Digite seu CPF: ")
    cpf = funcoes.valida_cpf(cpf)
    log.LogGeral(msg.info_cpf, cpf)

    if cpf == 'None':
        print('CPF inválido\n')
        log.LogGeral(msg.error_cpf_invalido, cpf)
        return

    # carrega o banco e checa se o cpf existe no banco
    check = db.carregarDB()
    check2 = db.checaDB(check, cpf)
    log.LogGeral(msg.info_db_checar, cpf)

    if check2:
        print("CPF já existe no sistema!\n")
        log.LogGeral(msg.error_cpf_existe, cpf)
        return
    # caso nao exista, registrar no sistema
    else:
        dic_dados['NOME'] = nome
        dic_dados['CPF'] = cpf
        print("CPF foi cadastrado no sistema!\n")
        log.LogGeral(msg.success_cadastro, nome, cpf)
        db.cadastrarDB(copy.deepcopy(dic_dados))

# funcao pra mostrar os dados do cliente na tela
def consulta_clientes():
    cpf = input("Digite seu CPF: ")

    # verificar se o cpf e valido
    cpf = funcoes.valida_cpf(cpf)
    log.LogGeral(msg.info_cpf, cpf)

    # carrega o banco e checa se o cpf existe no banco
    check = db.carregarDB()
    check2 = db.checaDB(check, cpf)
    log.LogGeral(msg.info_db_checar, cpf)
    if cpf == 'None':
        print("CPF inválido!\n")
        log.LogGeral(msg.error_cpf_invalido, cpf)
        return

    # se o cpf existir, printar na tela os dados
    if check2:
        db.consultaDB(check, cpf)
        log.LogGeral(msg.info_db_checar, cpf)

    if check2 == None:
        print("Este CPF não esta cadastrado!\n")
        log.LogGeral(msg.error_cpf_existe, cpf)
    return
    
# funcao que reserva a vaga do cpf cadastrado
def reservar_vaga():
    cpf = str(input('Digite seu CPF: '))

    # verificar se o cpf e valido
    cpf_formatado = funcoes.valida_cpf(cpf)
    log.LogGeral(msg.info_cpf)

    check = db.carregarDB()
    check2 = db.checaDB(check, cpf_formatado)
    log.LogGeral(msg.info_db_checar, cpf)
    
    if cpf_formatado == 'None':
        print("CPF inválido!\n")
        log.LogGeral(msg.error_cpf_invalido, cpf_formatado)
        return

    # checa se a pessoa ja tem vaga registrada
    for pessoa in check:
                if cpf_formatado in pessoa["CPF"]:
                    if pessoa["COLUNA"]:
                        print("Você já tem vaga!\n")
                        return     

    # checa se a pessoa ta cadastrada 
    if not check2:
        print("Voce não está cadastrado!")
        return

    else:
        matriz = db.carregarMDB()
        log.LogGeral(msg.info_mdb_carregar)
        print('-=' * 14)
        print('          Vagas')
        print('-=' * 14)
        for i in range(0, len(matriz)):
            print(', '.join(matriz[i]))
        print('-=' * 14, '\n')
        log.LogGeral(msg.success_interface)
    
        try:
            fileira = int(input('Digite a fileira: '))
            if 1 <= fileira <= 6:
                pass
            else:
                print('Fileira Inválida!\n')
                return

        except:
            print('Fileira Inválida!\n')
            return

        try:
            coluna = int(input('Digite a coluna: '))

            if 1 <= coluna <= 10:
                pass
            else:
                print('Coluna Inválida!\n')
                return
        except:
            print('Coluna Inválida!\n')
            return

        pass     
        # verifica se a vaga esta disponivel e faz a vaga
        if matriz[fileira - 1][coluna - 1] == 'X':
            print(f'Sua vaga foi reservada! | Fileira: {fileira} | Coluna: {coluna} | CPF: {cpf_formatado}')
            matriz[fileira - 1][coluna - 1] = '0'

            # alteracoes no banco de dados
            db.cadastrarMDB(matriz)
            log.LogGeral(msg.success_mdb_alterar)

            db.modificarDB(cpf_formatado, fileira, coluna)
            log.LogGeral(msg.success_db_alterar)
            
            check = db.carregarDB()

            log.relatorioDeReserva(check, cpf_formatado)
            log.relatorioVagaLivre()

        elif matriz[fileira - 1][coluna - 1] == '0':
            print('Esta vaga já está reservarda! | Escolha outra!\n')
            log.LogGeral(msg.warning_vaga, fileira, coluna)
            return

    # Print do Estacionamento (Matriz) para verificar visualmente
    print('-=' * 14)
    for i in range(0, len(matriz)):
        print(', '.join(matriz[i]))
    print('-=' * 14, '\n')
    log.LogGeral(msg.success_interface)

# funcao que cancela reserva do cliente
def cancelamento_reserva():
    cpf = str(input('Digite o CPF: '))

    # verifica se o cpf e valido
    cpf_formatado = funcoes.valida_cpf(cpf)
    log.LogGeral(msg.info_cpf, cpf_formatado)

    # carrega o banco
    check = db.carregarDB()
    matriz = db.carregarMDB()
    check2 = db.checaDB(check, cpf_formatado)

    if cpf_formatado == 'None':
        print("CPF inválido!\n")
        log.LogGeral(msg.error_cpf_invalido)
        return True

    if not check2:
        print("CPF não foi cadastrado!\n")
        log.LogGeral(msg.error_cpf_existe, cpf)
        return True


    fileirinha = ''
    coluninha = ''
    # verifica se a pessoa tem vaga pra cancelar
    for pessoa in check:
        if cpf_formatado in pessoa['CPF']:
            if pessoa['FILEIRA'] and pessoa['COLUNA']:
                fileirinha, coluninha = pessoa['FILEIRA'], pessoa['COLUNA']
                pessoa['FILEIRA'] = ''
                pessoa['COLUNA'] = ''
                fileirinha = int(fileirinha)
                coluninha = int(coluninha)

                # atualiza o banco de dados
                db.modificarDB(cpf_formatado, '', '', coluninha, fileirinha, cancela=True)
                log.LogGeral(msg.success_db_alterar)

                matriz[fileirinha - 1][coluninha - 1] = 'X'
                db.cadastrarMDB(matriz)
                log.LogGeral(msg.success_mdb_alterar)

                log.relatorioCancelamentoReserva()
                log.relatorioVagaLivre()

                print('Sua reserva foi cancelada com sucesso!')
                print('-=' * 14)
                for i in range(0, len(matriz)):
                    print(', '.join(matriz[i]))
                print('-=' * 14, '\n')
                log.LogGeral(msg.success_interface)
                return True

            else:
                print('Voce não tem vaga registrada!\n')
                log.LogGeral(msg.warning_no_vaga, cpf_formatado)
                return


if __name__ == '__main__':
    pass
