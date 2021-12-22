# Importacoes
from datetime import datetime
from database import db

# Funcao para registrar o log de dados
def LogGeral(msg, *var):
    with open("relatorios/relatorio.txt", "a+") as file:
        if var:
            file.write(f"{datetime.today().strftime('%d-%m-%Y-%H:%M:%S')} : {msg} {var}")
            file.write("\n")

        else:
            file.write(f"{datetime.today().strftime('%d-%m-%Y-%H:%M:%S')} : {msg}")
            file.write("\n")

# funcao que cria o relatorio de vagas livres
def relatorioVagaLivre():
    # Carrega o banco de dados da matriz e depois registra no arquivo vagalivre.txt
    matriz = db.carregarMDB()
    with open("relatorios/vagalivre.txt", "a+") as file:
        file.write("Relatorio De Vagas Livres | (X) Livre (O) Reservada\n")
        for i in range(0, len(matriz)):
            file.write('    '.join(matriz[i]))
            file.write("\n")
        file.write('-=' * 14)
        file.write(datetime.today().strftime('%d-%m-%Y-%H:%M:%S'))
        file.write("\n")

# funcao que cria o relatorio de cancelamento de reservas
def relatorioCancelamentoReserva():
    # carrega o banco de dados e registra no arquivo cancelamentoreserva.txt apenas os que cancelaram reserva
    check = db.carregarDB()
    for pessoa in check:
        # checa se a pessoa cancelou
        if pessoa["CANCELA"] == 'TRUE':
            with open("relatorios/cancelamentoreserva.txt", "a+") as file:
                file.write("-="*19)
                file.write("\n")
                file.write(f"Nome: {pessoa['NOME']}\n")
                file.write(f"CPF: {pessoa['CPF']}\n")
                file.write(f"Fileira: {pessoa['FILEIRACANCELADA']}\n")
                file.write(f"Coluna: {pessoa['COLUNACANCELADA']}\n")
                file.write(f"Cancelou Reserva as {datetime.today().strftime('%d-%m-%Y-%H:%M:%S')}\n")
                file.write("-="*19)
                file.write("\n")
    # muda a variavel CANCELA para false
    db.dbFalse()
# funcao que cria o relatorio de reservas
def relatorioDeReserva(info, cpf):
    # carrega o banco de dados e registra no arquivo reserva.txt apenas as pessoas que fizeram reserva
    for pessoa in info:
        if pessoa["CPF"] == cpf:
            with open("relatorios/reserva.txt", "a+") as file:
                file.write("-="*19)
                file.write("\n")
                file.write(f"Nome: {pessoa['NOME']}\n")
                file.write(f"CPF: {pessoa['CPF']}\n")
                file.write(f"Fileira: {pessoa['FILEIRA']}\n")
                file.write(f"Coluna: {pessoa['COLUNA']}\n")
                file.write(f"Fez reserva as {datetime.today().strftime('%d-%m-%Y-%H:%M:%S')}\n")
                file.write("-="*19)
                file.write("\n")
            return
            
