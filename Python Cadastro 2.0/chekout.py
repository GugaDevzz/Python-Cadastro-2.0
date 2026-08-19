from conectar_json import salvar_usuario, carregar_usuarios
import cores_modelos
import hashlib
import uuid
import os

def criptografia_livre(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

class Aluno:
    def __init__(self, nome_completo, turmacurso, responsavel, senha):
        self.chave = str(uuid.uuid4())[:6].upper()
        self.nome_completo = nome_completo
        self.turmacurso = turmacurso
        self.responsavel = responsavel
        self.senha = self.criptografar(senha)

    def criptografar(self, senha):
        return hashlib.sha256(senha.encode()).hexdigest()

    def cadastrando(self):
        openjson = carregar_usuarios() 

        for chave, dados in openjson.items():
            if dados["nome"] == self.nome_completo:
                exibir = cores_modelos.exibir_mensagem("Esse aluno ja existe!", "erro")
                aguardar = cores_modelos.aguardar_usuario()
                return False # Para a função aqui mesmo se achar

        # Se o loop terminar e não der 'return False', significa que não existe
        salvar_usuario(self.chave, self.nome_completo, self.turmacurso, self.responsavel, self.senha)
        os.system('cls' if os.name == 'nt' else 'clear')
        exibir = cores_modelos.exibir_mensagem("Aluno cadastrado com sucesso!", "sucesso")
        aguardar = cores_modelos.aguardar_usuario()
        return True


    def logando(self):
        openjson = carregar_usuarios()
        
        for chave, dados in openjson.items():
            if dados["nome"] == self.nome and dados["senha"] == self.senha:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"Olá {self.nome}, bem vindo ao banco python!")
                return True
        else:
        # O print de erro fica FORA do loop. Se rodar o loop inteiro e não achar, cai aqui.
            print("Usuário inexistente.")
            return False