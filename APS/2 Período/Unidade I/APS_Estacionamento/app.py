# Importacoes
import settings
import log
import time
from database import db
import os
from utils import funcoes, messages as msg


# Selecao do menu
menu = [1, 2, 3, 4, 5, 6, 7, 8, 9]
opcoesdomenu = [settings.cadastro, settings.consulta_clientes, settings.reservar_vaga, settings.cancelamento_reserva,
                funcoes.menu5, funcoes.menu6, funcoes.menu7, "SAIR", funcoes.menu128]


log.LogGeral(msg.info_entrada)

# Checa se o banco foi criado, caso nao exista ele inicializa (so acontece uma vez)
if not os.path.exists("database\data.pkl"):
    db.inicializarDB()

# Checa se a matriz foi criada, caso nao exista ele inicializa (so acontece uma vez)
if not os.path.exists("database\matriz.pkl"):
    db.inicializarMDB()

# Menu principal
while True:
    print("\n")
    print('-=' * 14)
    print('       Estacionamento')
    print('-=' * 14)

    print("[1] Cadastro De Cliente(Nome, CPF)\n"
          "[2] Consulta De Clientes (Pelo CPF)\n"
          "[3] Reserva De Vaga (Fileira, Vaga e CPF Do Cliente)\n"
          "[4] Cancelamento De Reserva (Pelo CPF Do Cliente)\n"
          "[5] Relatorio De Reservas (Vagas + Cliente Que Reservou)\n"
          "[6] Relatorio De Vagas Livres\n"
          "[7] Relatorio De Cancelamento De Reservas De Vagas\n"
          "[8] Sair\n")

    escolha = input("INPUT:")
    log.LogGeral(msg.info_input, escolha)


    if escolha.isnumeric():
        if int(escolha) == 8:            
            break

        if int(escolha) in menu:
            # Roda a funcao correta dependo da escolha do menu
            res = opcoesdomenu[int(escolha)-1]()

        else:
            print("Digite apenas de 1 a 8!\n")
            log.LogGeral(msg.error_input, escolha)

    else:
        print("Digite apenas digitos para acessar o menu!\n")
        log.LogGeral(msg.error_input, escolha)

    time.sleep(1)

# Fim da execucao
print("Volte Sempre!")
log.LogGeral(msg.info_saida)
