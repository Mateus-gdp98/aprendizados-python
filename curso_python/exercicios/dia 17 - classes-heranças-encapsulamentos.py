class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        print(f'Olá, meu nome é {self.nome} e idade {self.idade}')

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula, curso):
        super().__init__(nome, idade)
        self.curso = curso
        self.matricula = matricula
        print(f'Olá, meu nome é {self.nome} e idade {self.idade}, sou aluno (a) do curso {self.curso} e minha matricula é {self.matricula}.')

pessoa1 = Aluno("Mateus", 26, 5585, "Ciências")
        