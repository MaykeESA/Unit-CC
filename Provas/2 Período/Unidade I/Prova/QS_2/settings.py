# Importacoes
import re
from database import db
from utils import funcoes
import copy
from log import log

# Molde de registro de veterinario e pets
dic_dados_vet = {
    'NOME': '',
    'CPF': '',
    'CFMV': '',
    'SEXO': '',
    'STATUS': '',
}

dic_dados_pet = {
    'NOME': '',
    'CODIGO': '',
    'ESPECIE': '',
    'STATUS': '',
    'DATA': '',
    'CFMV': '',
}

# Função que cadastra veterinario (CFMV, Nome, CPF, Sexo, Status do Vet)
def cadastro_vet():
    nome = input("Digite seu nome: ")

    cpf = input("Digite seu CPF: ")
    cpf_formatado = funcoes.valida_cpf(cpf)
    if cpf_formatado == 'None':
        print('CPF inválido\n')
        return
    
    check = db.carregar_PDB()
    checkcpf = db.checacpf_PDB(check, cpf_formatado)

    if checkcpf:
        print("CPF já existe no sistema!\n")
        return
    else:
        cfmv = input("Digite seu CFMV: ")
        checkcfmv = db.checacfmv_PDB(check, cfmv)
        
        if cfmv.isnumeric():
            pass
        else:
            print("Valor inválido!\n")
            return
                
        if checkcfmv:
            print("CFMV já existe no sistema!\n")
            return
        else:  
            while True:
                #Input do Sexo mais verificação
                sexo = input("Digite seu sexo:\n"
                            "[1] Masculino\n"
                            "[2] Feminino\n"
                            "INPUT: ")
                if sexo == "1":
                    valor_sexo = "Masculino"
                    dic_dados_vet['SEXO'] = valor_sexo
                    break
                elif sexo == "2":
                    valor_sexo = "Feminino"
                    dic_dados_vet['SEXO'] = valor_sexo
                    break
                else:
                    print("Valor Inválido!")
                    continue

            while True:
                #Input do Status mais verificação
                status = input("Digite seu status:\n"
                        "[1] Ativo\n"
                        "[2] Inativo\n"
                        "INPUT: ")
                if status == "1":
                    valor_status = True
                    dic_dados_vet['STATUS'] = valor_status
                    break
                elif status == "2":
                    valor_status = False
                    dic_dados_vet['STATUS'] = valor_status
                    break
                else:
                    print("Valor Inválido!")
                    continue
            
            dic_dados_vet['NOME'] = nome
            dic_dados_vet['CPF'] = cpf_formatado
            dic_dados_vet['CFMV'] = cfmv
        
            db.cadastrar_PDB(copy.deepcopy(dic_dados_vet))

# Função que inativa veterinario (CPF)          
def mudar_status_vet():
    cpf = input("Digite seu CPF: ")
    cpf_formatado = funcoes.valida_cpf(cpf)

    if cpf_formatado == 'None':
        print('CPF inválido\n')
        return

    check = db.carregar_PDB()
    checkcpf = db.checacpf_PDB(check, cpf_formatado)

    if checkcpf:
        db.mudarStatusVet_PDB(cpf_formatado)
        print(f"Você foi inativado!\n")

    else:
        print(f"CPF não cadastrado no sistema!\n")
        return

# Função que cadastra o Pet (Código de Registro do Pet, Nome, Espec)
def cadastro_pet():
    codRe = input("Digite Codigo Registro: ")

    check = db.carrega_ADB()
    checkcode = db.checaCode_ADB(check, codRe)

    if checkcode:
        print("Codigo já existe no sistema\n")
        return

    else:
        nome = input("Digite Nome Pet: ")

        while True:
            espc = input("Digite a especie:\n"
                            "[1]Cachorro\n"
                            "[2]Gato\n"
                            "[3]Passaro\n"
                            "INPUT: " )
            if  espc == "1":
                valor_espc = "Cachorro"
                dic_dados_pet['ESPECIE'] = valor_espc
                break
            elif espc == "2":
                valor_espc = "Gato"
                dic_dados_pet['ESPECIE'] = valor_espc  
                break
            elif espc == "3":
                valor_espc = "Passaro"
                dic_dados_pet['ESPECIE'] = valor_espc
                break
            else:
                print("Digite um número válido!")          
            continue

        dic_dados_pet["NOME"] = nome
        dic_dados_pet["CODIGO"] = codRe

        db.cadastrar_ADB(copy.deepcopy(dic_dados_pet))

# Função que registra consulta (Data, CFMV, Código de Registo do Pet)
def registrar_consulta():
    check_animal = db.carrega_ADB()
    check = db.carregar_PDB()

    data = input('Digite a data da consulta (DD/MM/AAAA): ')
    data_validada = funcoes.valida_data(data)
    if not data_validada:
        print("Data inválida!")
        return

    else:
        cfmv = input("Digite o CFMV: ")
        cfmv_validado = db.checacfmv_PDB(check, cfmv)

        if cfmv_validado:
            for vet in check:
                if vet['STATUS']:                    
                    codRe = input("Digite Codigo de Registro: ")
                    checkcode = db.checaCode_ADB(check_animal, codRe)
                    if checkcode:
                        for status in check_animal:
                            if codRe == status["CODIGO"]:
                                if status['STATUS']:
                                    print('Já existe uma consulta para este animal!')
                                    return
                                else:
                                    valor_consulta = 0
                                    for animal in check_animal:
                                        if animal['ESPECIE'] == 'Cachorro':
                                            valor_consulta= '100'
                                            dic_dados_pet['VALOR'] = valor_consulta
                                        if animal['ESPECIE'] == 'Gato':
                                            valor_consulta = '120'
                                            dic_dados_pet['VALOR'] = valor_consulta
                                        if animal['ESPECIE'] == 'Passaro':
                                            valor_consulta = '150'
                                            dic_dados_pet['VALOR'] = valor_consulta
                                    dic_dados_pet['STATUS'] = True
                                    dic_dados_pet['DATA'] = data
                                    dic_dados_pet['CFMV'] = cfmv                     
                                    print('Consulta Registrada!\n')
                                    db.consulta_ADB(check_animal, codRe, data_validada, valor_consulta, cfmv, True)
                                    return
                    else:
                        print('Código de Registro Inexistente!\n')
                        return
                else:
                    print('Status do Veterinário Inativo!\n')
                    return
        else:
            print("Não existe ninguem com esse CFMV!\n")

# Função que cancela a consulta (Data, CFMV, Código de Registro do Pet)
def cancelar_consulta():
    check_animal = db.carrega_ADB()
    check = db.carregar_PDB()

    data = input('Digite da data da consulta (DD/MM/AAAA): ')
    data_validada = funcoes.valida_data(data)
    checkdata = db.checaData_ADB(check_animal, data_validada)

    if not checkdata:
        print("Essa data não tem reservas!\n")
        return
    else:
        cfmv = input("Digite seu CFMV: ")
        check_cfmv = db.checacfmv_PDB(check, cfmv)
        if not check_cfmv:
            print(" Nâo tem ninguém com esse CFMV!\n")
            return
        else:
            for vet in check:
                if vet['STATUS']:
                    codRe = input("Digite Codigo Registro: ")
                    check_code = db.checaCode_ADB(check_animal, codRe)
                    if not check_code:
                        print("Não tem animal com esse código!\n")
                        return
                    else:
                        db.consulta_ADB(check_animal, codRe, '', '', '', False)
                        print("Consulta cancelada!")
                        return
                else:
                    print('Status do veterinário Inativo!')
                    return


def relatorio_pet():
    load = db.carrega_ADB()

    for animal in load:
        print("-="*15)
        print(f"Nome: {animal['NOME']}")
        print(f"Codigo: {animal['CODIGO']}")
        print(f"Especie: {animal['ESPECIE']}")
        print("-="*15)

    log.logPet()

def relatorio_veterinario_ativo():
    load = db.carregar_PDB()

    for pessoa in load:
        if pessoa["STATUS"]:
            print("-="*15)
            for key, value in pessoa.items():
                print(f"{key}: {value}")
            print("-="*15)
    
    log.logVet()

def relatorio_consulta_data():
    valor_total = 0
    load = db.carrega_ADB()
    check_pessoa = db.carregar_PDB()

    data = input('Digite da data da consulta (DD/MM/AAAA): ')
    data_validada = funcoes.valida_data(data)
    if not data_validada:
        print("Data invalida")
    
    else:
        checkdata = db.checaData_ADB(load, data_validada)

        if checkdata:
            for animal in load:
                if animal["DATA"] == data_validada:
                    valor_total += int(animal["VALOR"])
                    cfmv_compara = animal["CFMV"]
                    for dados_vet in check_pessoa:
                        if cfmv_compara == dados_vet['CFMV']:
                            print("-="*15)
                            print(f"Veterinario: {dados_vet['NOME']} CFMV: {dados_vet['CFMV']} Data Consulta: {animal['DATA']}")
                            print(f"Animal: {animal['NOME']} Codigo: {animal['CODIGO']} Valor Consulta: {animal['VALOR']}")
                            if animal["STATUS"]:
                                print(f"Status: Ativo")
                            else:
                                print(f"Status: Inativo")
                            print("-="*15)
            print(f"Valor total arrecadado na data {data_validada} = R${valor_total}")
        else:
            print("essa data nao tem reservas")

        log.logData(data_validada)


    
