import time
import os
from chekout import carregar_usuarios
from verificacao_dados import tratamento_visual_criar, tratamento_visual_alterar
from chekout import criptografia_livre
COR_RESET = "\033[0m"
COR_NEGRITO = "\033[1m"
COR_AZUL = "\033[94m"
COR_VERDE = "\033[92m"
COR_AMARELO = "\033[93m"
COR_VERMELHO = "\033[91m"
COR_REVERSO = "\033[7m"

# FEITO PARA TIME.SLEEP, TRATAMENTO VISUAL, QUANDO O OS.SYSTEM ACONTECE LOGO APOS CONTINUA O MENU DE ALTERAR

#---------------------------------------------------------------------------------
#TRATAMENTO DO INPUT, OQUE PODE E NÃO PODE, LOGICA DE SEGURANÇA E CONFIRMAÇÃO
#---------------------------------------------------------------------------------

def nomeando_criar():
    while True:
        nome = input(f"  {COR_AZUL}»{COR_RESET} Nome Completo: ").strip()
        if len(nome) > 25:
            print(f"{COR_AMARELO}{COR_NEGRITO}  ATENÇÃO: {COR_RESET}{COR_AMARELO}O nome {nome} execeu \na quantidade de caractéres.")
            time.sleep(4.0)
            os.system('cls' if os.name == 'nt' else 'clear')
            tratamento_visual_criar()

        elif len(nome) < 5:
            print(f"{COR_AMARELO}{COR_NEGRITO}  ATENÇÃO: {COR_RESET}{COR_AMARELO}Digite ao menos o primeiro e o segundo nome.")
            time.sleep(4.0)
            os.system('cls' if os.name == 'nt' else 'clear')
            tratamento_visual_criar()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            tratamento_visual_criar()
            return(nome)


def turmando_criar():
    turmas = {
    "1": "TI36",
    "2": "TI34",
    "3": "TI39",
    }

    while True:
        print(f"  {COR_AZUL}»{COR_RESET} Nova turma:\n ")
        for chave, valor in turmas.items():
            print(f"  {COR_VERDE}({chave}){COR_RESET} ── {valor}")
        escolha_turma = input(f"\n{COR_NEGRITO}  SELECIONE A TURMA: {COR_RESET}").strip()

        for chave, valor in turmas.items():
            if chave == escolha_turma:
                opcao = valor
                print(f" A turma {COR_NEGRITO}{COR_VERDE}{opcao} {COR_RESET}foi selecionada!")
                time.sleep(3.0)
                os.system('cls' if os.name == 'nt' else 'clear')
                tratamento_visual_criar()
                return(opcao)
        if escolha_turma == "":
            print(f"{COR_AMARELO}{COR_NEGRITO}TENTE NOVAMENTE: {COR_RESET}{COR_AMARELO}Digite o número refente a turma desejada.")
            time.sleep(3.0)
            # opcao = valor
            os.system('cls' if os.name == 'nt' else 'clear')
            tratamento_visual_criar()


def nomeando_responsavel_criar():
    while True:
        responsavel = input(f"  {COR_AZUL}»{COR_RESET} Nome do Responsável: ").strip()
        if len(responsavel) > 25:
            print(f"{COR_AMARELO}{COR_NEGRITO}ATENÇÃO: {COR_RESET}{COR_AMARELO}O nome {responsavel} execeu a quantidade de caractéres. \nDigite apenas o primeiro e segundo nome do responsável.")
            time.sleep(4.0)
            os.system('cls' if os.name == 'nt' else 'clear')
            tratamento_visual_criar()

        elif len(responsavel) < 5:
            print(f"{COR_AMARELO}{COR_NEGRITO}ATENÇÃO: {COR_RESET}{COR_AMARELO}Digite ao menos o primeiro e o segundo nome do responsável.")
            time.sleep(4.0)
            os.system('cls' if os.name == 'nt' else 'clear')
            tratamento_visual_criar()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            tratamento_visual_criar()
            return (responsavel)

def validar_senha_criar():
    while True:
        senha = input(f"  {COR_AZUL}»{COR_RESET} Senha: ").strip()
        if senha == "":
            print(f"{COR_AMARELO}{COR_NEGRITO}ATENÇÃO: {COR_RESET}{COR_AMARELO} Sua senha não pode ser um campo vazio")
            os.system('cls' if os.name == 'nt' else 'clear')
            tratamento_visual_criar()
        elif len(senha) > 10 or len(senha) < 4:
            print(f"{COR_AMARELO}{COR_NEGRITO}ATENÇÃO: {COR_RESET}{COR_AMARELO} Sua senha deve conter entre 4 a 10 caractéres")
            os.system('cls' if os.name == 'nt' else 'clear')
            tratamento_visual_criar()
        else:
            return (senha)

#CRIAR<--

#----------------------------------------------------------------------------------------------------------------

#EDITAR<--

def nomeando_editar(novo_nome):
    from cores_modelos import exibir_cabecalho

    while True:
        if len(novo_nome) > 25:
            print(f"{COR_AMARELO}{COR_NEGRITO}ATENÇÃO: {COR_RESET}{COR_AMARELO}O nome {novo_nome} execeu \na quantidade de caractéres.")
            time.sleep(3.0)
            os.system('cls' if os.name == 'nt' else 'clear')
            tratamento_visual_alterar()
            return False

        elif len(novo_nome) > 1 and len(novo_nome) < 5:
            print(f"{COR_AMARELO}{COR_NEGRITO}AVISO: {COR_RESET}{COR_AMARELO}Digite ao menos o primeiro e o segundo nome do responsável (< 5).")
            time.sleep(3.0)
            os.system('cls' if os.name == 'nt' else 'clear')
            tratamento_visual_alterar()
            return False

        elif (novo_nome) == "":
            os.system('cls' if os.name == 'nt' else 'clear')
            tratamento_visual_alterar()
            return True
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            tratamento_visual_alterar()
            return True



def turmando_editar(opcao):

    turmas = {
    "1": "TI36",
    "2": "TI34",
    "3": "TI39",
    }

    while True:
        print(f"{COR_AZUL}»{COR_RESET} Nova turma [{COR_AZUL}{opcao}{COR_RESET}]:\n ")
        for chave, valor in turmas.items():
            print(f"  {COR_VERDE}({chave}){COR_RESET} ── {valor}")
        escolha_turma = input(f"\n{COR_NEGRITO} SELECIONE A TURMA: {COR_RESET}").strip()

        for chave, valor in turmas.items():
            if chave == escolha_turma:
                opcao = valor
                print(f" A turma {COR_NEGRITO}{COR_VERDE}{opcao} {COR_RESET}foi selecionada!")
                os.system('cls' if os.name == 'nt' else 'clear')
                tratamento_visual_alterar()
                return(opcao)
        if escolha_turma == valor or escolha_turma =="":
            os.system('cls' if os.name == 'nt' else 'clear')
            tratamento_visual_alterar()
            return(opcao)


def nomeando_responsavel_editar(novo_responsavel):

    while True:
        if len(novo_responsavel) > 50:
            print(f"{COR_AMARELO}{COR_NEGRITO}ATENÇÃO: {COR_RESET}{COR_AMARELO}O nome {novo_responsavel} execeu \na quantidade de caractéres.")
            time.sleep(4.0)
            os.system('cls' if os.name == 'nt' else 'clear')
            tratamento_visual_alterar()
            return False

        elif len(novo_responsavel) > 1 and len(novo_responsavel) < 5:
            print(f"{COR_AMARELO}{COR_NEGRITO}AVISO: {COR_RESET}{COR_AMARELO}Digite ao menos o primeiro e o segundo nome do responsável (< 5).")
            time.sleep(4.0)
            os.system('cls' if os.name == 'nt' else 'clear')
            tratamento_visual_alterar()
            return False

        elif (novo_responsavel) == "":
            os.system('cls' if os.name == 'nt' else 'clear')
            tratamento_visual_alterar()
            return True
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            tratamento_visual_alterar()
            return True
        
def validar_senha_editar(senha):
    while True:
        nova_senha = input(f"Nova senha [{COR_AZUL}{senha}{COR_RESET}]: ").strip()
        if len(nova_senha) > 10 or len(nova_senha) < 4:
            print(f"{COR_AMARELO}{COR_NEGRITO}ATENÇÃO: {COR_RESET}{COR_AMARELO} Sua senha deve conter entre 4 a 10 caractéres")
            os.system('cls' if os.name == 'nt' else 'clear')
            tratamento_visual_alterar()
        elif nova_senha == "":
            os.system('cls' if os.name == 'nt' else 'clear')
            tratamento_visual_alterar()   
            return(senha)
        else:         
            nova_senha_cripto = criptografia_livre(nova_senha)
            return(nova_senha_cripto)  
