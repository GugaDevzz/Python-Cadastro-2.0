# aqui voce vai passar aquelas verificaçoes, se o nome foi digitado ent coloque um certinho, trabalhe com essa logica
# faça tambem o print, se caso o cliente errou algum dado, para entrar com seu ra no campo de editar, essa mensagem logo apos o termino do cadastro
COR_RESET = "\033[0m"
COR_NEGRITO = "\033[1m"
COR_AZUL = "\033[94m"
COR_VERDE = "\033[92m"
COR_AMARELO = "\033[93m"
COR_VERMELHO = "\033[91m"
COR_REVERSO = "\033[7m"

# Use a base desse def para colocar as confirmações, ou crie outro igual para deixar apenas os primeiros elementos e depois outro para as confirmações de que os campos foram preenchidos
# FEITO PARA TIME.SLEEP, TRATAMENTO VISUAL, QUANDO O OS.SYSTEM ACONTECE LOGO APOS CONTINUA O MENU DE ALTERAR
def tratamento_visual_criar():
    from cores_modelos import exibir_cabecalho
    exibir_cabecalho("NOVO CADASTRO DE ALUNO")
    
    print(f"{COR_NEGRITO}Preencha os dados do estudante:{COR_RESET}\n")

def tratamento_visual_alterar():
    from cores_modelos import exibir_cabecalho
    exibir_cabecalho("ALTERAR DADOS DO ALUNO")
    print(f"{COR_NEGRITO}Preencha os dados do estudante:{COR_RESET}\n")
