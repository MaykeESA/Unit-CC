# Importacoes
import re
from database import db
from utils import funcoes
import copy

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
    'CODE': '',
    'ESPC': '',
    'STATUS': '',
    'DATA': '',
}

# Função que cadastra veterinario (CFMV, Nome, CPF, Sexo, Status do Vet)
def cadastro_vet():
    
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")
    cpf_formatado = funcoes.valida_cpf(cpf)
    if cpf_formatado == 'None':
        print('CPF inválido\n')
        return
    
    check = db.carregarDB()
    checkcpf = db.checacpfDB(check, cpf_formatado)

    if checkcpf:
        print("CPF já existe no sistema!\n")
        return
    else:
        cfmv = input("Digite seu CFMV: ")
        checkcfmv = db.checacfmvDB(check, cfmv)
        
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
        
            db.cadastrarDB(copy.deepcopy(dic_dados_vet))

# Função que inativa veterinario (CPF)          
def mudar_status_vet():
    cpf = input("Digite seu CPF: ")
    cpf_formatado = funcoes.valida_cpf(cpf)

    check = db.carregarDB()
    checkcpf = db.checacpfDB(check, cpf_formatado)

    if checkcpf:
        db.mudarstatus_vetDB(check, cpf_formatado)
        
        print(f"Você foi inativado!\n")

    else:
        print(f"CPF não cadastrado no sistema!\n")
        return

# Função que cadastra o Pet (Código de Registro do Pet, Nome, Espec)
def cadastro_pet():
    codRe = input("Digite Codigo Registro: ")
    nome = input("Digite Nome Pet: ")

    check = db.carrega_ADB()
    checkcode = db.checacode_ADB(check, codRe)

    if checkcode:
        print("Codigo já existe no sistema\n")
        return

    else:
        while True:
            espc = input("Digite a especie:\n"
                            "[1]Cachorro\n"
                            "[2]Gato\n"
                            "[3]Passaro\n"
                            "INPUT: " )
            if  espc == "1":
                valor_espc = "Cachorro"
                dic_dados_pet['ESPC'] = valor_espc
                break
            elif espc == "2":
                valor_espc = "Gato"
                dic_dados_pet['ESPC'] = valor_espc  
                break
            elif espc == "3":
                valor_espc = "Passaro"
                dic_dados_pet['ESPC'] = valor_espc
                break
            else:
                print("Digite um número válido!")          
            continue

        dic_dados_pet["NOME"] = nome
        dic_dados_pet["CODE"] = codRe

        db.cadastrar_ADB(copy.deepcopy(dic_dados_pet))


# Função que registra consulta (Data, CFMV, Código de Registo do Pet)
def registrar_consulta():
    check_animal = db.carrega_ADB()
    check = db.carregarDB()

    data = input('Digite da data da consulta (DD/MM/AAAA): ')
    data_validada = funcoes.valida_data(data)
    if not data_validada:
        print("Data inválida!")
        return
    else:
        cfmv = input("Digite seu CFMV: ")
        cfmv_validado = db.checacfmvDB(check, cfmv)

        if cfmv_validado:
            for vet in check:
                if vet['STATUS']:
                    codRe = input("Digite Codigo de Registro: ")
                    checkcode = db.checacode_ADB(check_animal, codRe)
                    if checkcode:
                        valor_consulta = 0
                        for animal in check_animal:
                            if animal['ESPC'] == 'Gato':
                                valor_consulta= '120'
                                dic_dados_pet['VALOR'] = valor_consulta
                            if animal['ESPC'] == 'Passaro':
                                valor_consulta = '100'
                                dic_dados_pet['VALOR'] = valor_consulta
                            if animal['ESPC'] == 'Cachorro':
                                valor_consulta = '150'
                                dic_dados_pet['VALOR'] = valor_consulta
                        dic_dados_pet['STATUS'] = True
                        dic_dados_pet['DATA'] = data                     
                        print('Consulta Registrada!\n')
                        db.consulta_ADB(check_animal, codRe, data_validada, valor_consulta, True)
                        return
                    else:
                        print('Código de Registro Inexistente!\n')
                        return
                else:
                    print('Status do Veterinário Inativo!\n')
                    return


# Função que cancela a consulta (Data, CFMV, Código de Registro do Pet)
def cancelar_consulta():
    check_animal = db.carrega_ADB()
    check = db.carregarDB()

    data = input('Digite da data da consulta (DD/MM/AAAA): ')
    data_validada = funcoes.valida_data(data)
    checkdata = db.checadata_ADB(check_animal, data_validada)

    if not checkdata:
        print("Essa data não tem reservas!\n")
        return
    else:
        cfmv = input("Digite seu CFMV: ")
        check_cfmv = db.checacfmvDB(check, cfmv)
        if not check_cfmv:
            print(" Nâo tem ninguém com esse CFMV!\n")
            return
        else:
            for vet in check:
                if vet['STATUS']:
                    codRe = input("Digite Codigo Registro: ")
                    check_code = db.checacode_ADB(check_animal, codRe)
                    if not check_code:
                        print("Não tem animal com esse código!")
                        return
                    else:
                        db.consulta_ADB(check_animal, codRe, '', '', False)
                        print("Consulta cancelada!")
                        return
                else:
                    print('Status do veterinário Inativo!')
                    return

    
def relatorio_pet():
    pass

def relatorio_veterinario_ativo():
    pass

def relatorio_consulta_data():
    pass