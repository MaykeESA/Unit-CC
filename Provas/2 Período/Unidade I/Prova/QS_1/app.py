# Importacoes
import time
import os
from database import db
import settings
from utils import funcoes

menu = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
opcoesdomenu = [settings.cadastro_vet, settings.mudar_status_vet, settings.cadastro_pet,
                settings.registrar_consulta, settings.cancelar_consulta, settings.relatorio_pet,
                settings.relatorio_veterinario_ativo, settings.relatorio_consulta_data, "SAIR", funcoes.menu10]

if not os.path.exists("database\data.pkl"):
    db.inicializarDB()

if not os.path.exists("database\pet.pkl"):
    db.inicializar_ADB()

while True:
    print("\n")
    print('-=' * 14)
    print('       Clínica Vetgay, apenas para animais trans e homossexuais')
    print('-=' * 14)

    print("[1] Cadastro de Veterinários\n"
          "[2] Inativação do cadastro do Veterinário\n"
          "[3] Cadastro de Pets\n"
          "[4] Registrar Consulta\n"
          "[5] Cancelar Consulta\n"
          "[6] Relatório de Pets\n"
          "[7] Relatório de Veterinários Ativos\n"
          "[8] Relatório de Consultas por Data\n"
          "[9] Sair")
        #COMO O CU DE BRENO

    inputmenu = input("INPUT:")
    # CU DE BRENO É MEU
    if inputmenu.isnumeric():
        if int(inputmenu) == 9:
            break

        if int(inputmenu) in menu:
            # Roda a funcao correta dependo da escolha do menu
            res = opcoesdomenu[int(inputmenu)-1]()

        else:
            print("Digite apenas de 1 a 10!\n")

    else:
        print("Digite apenas digitos para acessar o menu!\n")
        

    time.sleep(1)

# Fim da execucao
print("Volte Sempre!")
