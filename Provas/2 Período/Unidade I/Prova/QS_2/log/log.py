from database import db
from utils import funcoes


def logPet():
    load = db.carrega_ADB()
    with open('relatorio/todos_pet.txt', 'w') as file:
        for animal in load:
            file.write(f"{('-=')*15}\n")
            file.write(f"Nome: {animal['NOME']}\n")
            file.write(f"Codigo: {animal['CODIGO']}\n")
            file.write(f"Especie: {animal['ESPECIE']}\n")
            file.write(f"{('-=')*15}\n")


def logVet():
    load = db.carregar_PDB()
    with open('relatorio/vet_ativo.txt', 'w') as file:
        for pessoa in load:
            if pessoa["STATUS"]:
                file.write(f"{('-=')*15}\n")
                file.write(f"Nome: {pessoa['NOME']}\n")
                file.write(f"CFMV: {pessoa['CFMV']}\n")
                file.write(f"Sexo: {pessoa['SEXO']}\n")
                file.write(f"Status: Ativo\n")
                file.write(f"{('-=')*15}\n")
        


def logData(data):
    valor_total = 0
    load = db.carrega_ADB()
    check_pessoa = db.carregar_PDB()

    data_compara = data
    data_validada = funcoes.valida_data(data_compara)
    if not data_validada:
        return
    
    else:
        checkdata = db.checaData_ADB(load, data_validada)
        if checkdata:
            with open('relatorio/consulta_data.txt', 'w') as file:
                for animal in load:
                    if animal["DATA"] == data_validada:
                        valor_total += int(animal["VALOR"])
                        cfmv_compara = animal["CFMV"]
                        for dados_vet in check_pessoa:
                            if cfmv_compara == dados_vet['CFMV']:
                                file.write(f"{('-=')*15}\n")
                                file.write(f"Veterinario: {dados_vet['NOME']} CFMV: {dados_vet['CFMV']} Data Consulta: {animal['DATA']}\n")
                                file.write(f"Animal: {animal['NOME']} Codigo: {animal['CODIGO']} Valor Consulta: {animal['VALOR']}\n")
                                if animal["STATUS"]:
                                    file.write(f"Status: Ativo\n")
                                else:
                                    file.write(f"Status: Inativo\n")
                                file.write(f"{('-=')*15}\n")
                file.write(f"Valor total arrecadado na data {data_validada} = R${valor_total}\n")
        else:
            return



 

