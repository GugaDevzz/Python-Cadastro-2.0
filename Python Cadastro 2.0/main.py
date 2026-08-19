from cores_modelos import exibir_cabecalho, tela_alteracao, tela_busca, tela_cadastro, tela_exclusao, tela_listagem, tela_relatorios, exibir_mensagem
import time
import os
import traceback

COR_RESET = "\033[0m"
COR_NEGRITO = "\033[1m"
COR_AZUL = "\033[94m"
COR_VERDE = "\033[92m"
COR_AMARELO = "\033[93m"
COR_VERMELHO = "\033[91m"
COR_REVERSO = "\033[7m"

LARGURA_TELA = 65

def menu_principal():
    opcoes = {
        "1": "Cadastrar Aluno",
        "2": "Listar Alunos",
        "3": "Buscar Aluno",
        "4": "Alterar Dados",
        "5": "Excluir Aluno",
        # "6": "Relatórios Gerenciais",
        "0": "Sair do Sistema"
    }

    while True:
        exibir_cabecalho("SISTEMA DE CADASTRO ESCOLAR")
        
        print(f"{COR_NEGRITO} SELECIONE UMA OPERAÇÃO:{COR_RESET}\n")
        for chave, valor in opcoes.items():
            print(f"  {COR_AZUL}[{chave}]{COR_RESET} ── {valor}")
        print(f"\n{COR_AZUL}╶{'─' * (LARGURA_TELA - 2)}╴{COR_RESET}")
        
        opcao = input(f"\n{COR_NEGRITO}Escolha uma opção: {COR_RESET}").strip()

        if opcao == "1":
            tela_cadastro()
        elif opcao == "2":
            tela_listagem()
        elif opcao == "3":
            tela_busca()
        elif opcao == "4":
            tela_alteracao()
        elif opcao == "5":
        #     tela_exclusao()
        # elif opcao == "6":
            tela_relatorios()
        elif opcao == "0":
            exibir_cabecalho("SISTEMA ENCERRADO")
            print(f"{COR_VERDE}Alterações salvas. Até logo!{COR_RESET}")
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            exibir_mensagem("Opção inválida! Tente novamente.", "erro")
            time.sleep(1.5)

try:
    menu_principal()
except Exception as erro:
    print("\n=== OCORREU UM ERRO NO PROGRAMA ===")
    # Mostra exatamente a linha e o motivo do erro
    traceback.print_exc() 
    print("====================================")
    input("\nAperte ENTER para fechar...")

