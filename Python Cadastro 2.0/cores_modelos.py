import os
import time
from chekout import Aluno
from conectar_json import carregar_usuarios, salvar_usuario, Retorna_conteudo
from tratamento_input import nomeando_criar, turmando_criar, nomeando_responsavel_criar, nomeando_editar, turmando_editar, nomeando_responsavel_editar, validar_senha_criar, validar_senha_editar
from verificacao_dados import tratamento_visual_criar, tratamento_visual_alterar


#Cores ANSI
COR_RESET = "\033[0m"
COR_NEGRITO = "\033[1m"
COR_AZUL = "\033[94m"
COR_VERDE = "\033[92m"
COR_AMARELO = "\033[93m"
COR_VERMELHO = "\033[91m"
COR_REVERSO = "\033[7m"

LARGURA_TELA = 65

def exibir_cabecalho(titulo):
    """Gera um cabeçalho padrão elegante com linhas duplas."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{COR_AZUL}╔{'═' * (LARGURA_TELA - 2)}╗{COR_RESET}")
    texto_centralizado = titulo.center(LARGURA_TELA - 2)
    print(f"{COR_AZUL}║{COR_NEGRITO}{texto_centralizado}{COR_AZUL}║{COR_RESET}")
    print(f"{COR_AZUL}╚{'═' * (LARGURA_TELA - 2)}╝{COR_RESET}\n")

def aguardar_usuario():
    print(f"\n{COR_AMARELO}Pressione [Enter] para voltar ao menu...{COR_RESET}")
    input()

def exibir_mensagem(texto, tipo="info"):
    if tipo == "sucesso":
        print(f"\n{COR_VERDE}✔ {texto}{COR_RESET}")
    elif tipo == "erro":
        print(f"\n{COR_VERMELHO}✘ {texto}{COR_RESET}")
    else:
        print(f"\n{COR_AMARELO}ℹ {texto}{COR_RESET}")

# ──────────────────────────────────────────────────────────
# 1. TELA DE CADASTRO
# ──────────────────────────────────────────────────────────
def tela_cadastro():
    tratamento_visual_criar()
    
    # Inputs limpos e organizados
    while True:
        nome = nomeando_criar()
        break

    while True:
        turma_escolhida = turmando_criar()
        break

    while True:
        responsavel = nomeando_responsavel_criar()
        break
    
    while True:
        senha = validar_senha_criar()
        break

    novo_aluno = Aluno(nome, turma_escolhida, responsavel, senha)
    novo_aluno.cadastrando()   
    
# ──────────────────────────────────────────────────────────
# 2. TELA DE LISTAGEM (Tabela Alinhada)
# ──────────────────────────────────────────────────────────
def tela_listagem():
    exibir_cabecalho("LISTAGEM GERAL DE ALUNOS")
    alunos = carregar_usuarios()

    print(f"{COR_REVERSO}{' R.A. ':<9} │ {'Nome do Aluno':<30} │ {'Turma':<15} {COR_RESET}")

    for ra, dados in alunos.items():
        nome = dados["nome"]
        turma = dados["Turma/Curso"]
        print(f"{"─" * 10}┼{"─" * 32}┼{"─" * 17}")
        print(f" {ra:<8} │ {nome:<30} │ {turma:<15}")
    

    print(f"\n{COR_AZUL}Total de alunos cadastrados: {len(alunos)}{COR_RESET}")
    aguardar_usuario()

# ──────────────────────────────────────────────────────────
# 3. TELA DE BUSCA
# ──────────────────────────────────────────────────────────
def tela_busca():
    exibir_cabecalho("BUSCAR ESTUDANTE")
    ra_busca = input(f"Digite o {COR_NEGRITO}R.A.{COR_RESET} do aluno que deseja procurar: ").strip()
    alunos = carregar_usuarios()

    # Simulação da sua lógica de busca (se achar o aluno)
    if ra_busca in alunos:
        RA_aluno = alunos[ra_busca]
        nome = RA_aluno["nome"]
        curso = RA_aluno["Turma/Curso"]

        print(f"\n{COR_AZUL}┌─────────────────── FENDA DO ALUNO ───────────────────┐{COR_RESET}")
        print(f"  {COR_NEGRITO}R.A.:{COR_RESET} {ra_busca}")
        print(f"  {COR_NEGRITO}Nome:{COR_RESET} {nome}")
        print(f"  {COR_NEGRITO}Curso:{COR_RESET} {curso}")
        print(f"  {COR_NEGRITO}Status:{COR_RESET} {COR_VERDE}Regular / Matriculado{COR_RESET}")
        print(f"{COR_AZUL}└──────────────────────────────────────────────────────┘{COR_RESET}")
    else:
        exibir_mensagem("Aluno não encontrado no sistema.", "erro")
        
    aguardar_usuario()

# ──────────────────────────────────────────────────────────
# 4. TELA DE ALTERAÇÃO (Update)
# ──────────────────────────────────────────────────────────

def tela_alteracao():
    exibir_cabecalho("ALTERAR DADOS DO ALUNO")
    ra_busca = input(f"Digite o {COR_NEGRITO}R.A.{COR_RESET} para modificar: ").strip()
    
    alunos = carregar_usuarios()

    if ra_busca in alunos:
        RA_aluno = alunos[ra_busca]
        nome = RA_aluno["nome"]
        curso = RA_aluno["Turma/Curso"]
        responsavel = RA_aluno["responsavel"]
        senha = RA_aluno["senha"]

        print(f"\nAluno encontrado: {COR_NEGRITO}{nome}{COR_RESET}")
        print(f"{COR_AMARELO}(Deixe em branco para manter o dado atual){COR_RESET}\n")
        
        while True:
            novo_nome = input(f"{COR_AZUL}»{COR_RESET} Novo nome [{COR_AZUL}{nome}{COR_RESET}]: ").strip()
            if nomeando_editar(novo_nome):
                # tratamento para manter o dados atual do nome do responsavel
                if novo_nome == "":
                    novo_nome = nome
                break

        while True:
            nova_turma = turmando_editar(curso)
            break

        while True:
            novo_responsavel = input(f"{COR_AZUL}»{COR_RESET} Novo nome do responsável [{COR_AZUL}{responsavel}{COR_RESET}]: ").strip()
            if nomeando_responsavel_editar(novo_responsavel):
            # tratamento para manter o dados atual do nome do responsavel
                if novo_responsavel == "":
                    novo_responsavel = responsavel
                break

        while True:
            # tratamento para manter o dados atual da senha
            nova_senha = validar_senha_editar(senha)
            break

        salvar_usuario(ra_busca, novo_nome, nova_turma, novo_responsavel, nova_senha)
        exibir_mensagem("Dados atualizados com sucesso!", "sucesso")
    else:
        exibir_mensagem("R.A. não localizado.", "erro")
        
    aguardar_usuario()

# ──────────────────────────────────────────────────────────
# 5. TELA DE EXCLUSÃO (Deletar com Confirmação)
# ──────────────────────────────────────────────────────────
def tela_exclusao():
    exibir_cabecalho("EXCLUIR REGISTRO DE ALUNO")
    ra_busca = input(f"{COR_VERMELHO}⚠{COR_RESET} Digite o {COR_NEGRITO}R.A.{COR_RESET} para remoção: ").strip()
    alunos = carregar_usuarios()

    if ra_busca in alunos:
        RA_aluno = alunos[ra_busca]
        nome = RA_aluno["nome"]
        print(f"\n{COR_VERMELHO}ATENÇÃO:{COR_RESET} Você está prestes a deletar o aluno: {COR_NEGRITO}{nome}{COR_RESET}")
        confirmar = input(f"Confirma a exclusão permanente? ({COR_VERDE}S{COR_RESET}/{COR_VERMELHO}N{COR_RESET}): ").strip().upper()
        
        if confirmar == 'S':
            usuario_deletado = alunos.pop(ra_busca) 
            Retorna_conteudo(alunos)
            exibir_mensagem("Registro removido do sistema de forma definitiva.", "sucesso")
        else:
            exibir_mensagem("Operação cancelada pelo usuário.", "info")
    else:
        exibir_mensagem("Nenhum aluno encontrado com este R.A.", "erro")
        
    aguardar_usuario()

# ──────────────────────────────────────────────────────────
# 6. TELA DE RELATÓRIOS (Visão Estatística)
# ──────────────────────────────────────────────────────────
def tela_relatorios():
    exibir_cabecalho("RELATÓRIOS E ESTATÍSTICAS")
    alunos = carregar_usuarios()

    print(f"{COR_NEGRITO}RESUMO DO SISTEMA DE ENSINO{COR_RESET}\n")
    
    #precisa fazer uma relatarios sobre, quantos alunos em cada turma, turma co mais
    #estudantes, ativar ou desativar e mostrar quantos alunos ativos....
    
    aguardar_usuario()