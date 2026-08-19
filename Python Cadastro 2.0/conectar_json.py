import os
import json

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))

    # 2. Junta a pasta do script com o nome do arquivo JSON
ARQUIVO = os.path.join(DIRETORIO_ATUAL, "armazenar.json")

def carregar_usuarios():

        # 1. Descobre a pasta onde este arquivo .py está salvo
    if os.path.exists(ARQUIVO):

        # Abre o arquivo no modo leitura ("r")
        # encoding="utf-8" permite acentos e caracteres especiais
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo: #open é uma função nativa do python

            # Lê o conteúdo JSON do arquivo e converte para dicionário Python
            return json.load(arquivo) #load percente ao modulo json
        
    # Se o arquivo não existir, retorna dicionário vazio
    return {}


def salvar_usuario (RA, nome, turmacurso, responsavel, senha):
    usuarios = carregar_usuarios()

    usuarios[RA] = {
        "nome": nome,
        "Turma/Curso": turmacurso,
        "responsavel": responsavel,
        "senha": senha,
        }
    # Abre o arquivo no modo escrita ("w")
    # Se não existir, ele cria
    # Se existir, substitui o conteúdo antigo
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:

        # Converte o dicionário Python para JSON e salva no arquivo
        # indent=4 organiza visualmente com espaçamento
        # ensure_ascii=False mantém acentos normais
        json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)


def Retorna_conteudo(usuarios):
    with open("armazenar.json", "w", encoding="utf-8") as arquivo:
        json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)