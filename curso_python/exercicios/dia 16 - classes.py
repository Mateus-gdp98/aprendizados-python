# Criando a classe Pessoa
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        print(f'Objeto criado para {self.nome}')


# Criando uma instância da classe Pessoa
pessoa1 = Pessoa("Mateus", 26)
    
    