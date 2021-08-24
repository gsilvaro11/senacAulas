"""
Construa um algoritmo para implementar a classe Aluno(Código, nome, matrícula).
A classe Aluno possui duas subclasses, aluEnsinoMedio(ano) e AlunoGraduacao(semestre).

As 3 clases possuem o método construtor e também o método imprimir(), que imprime na tela\n
os atributos da sua classe
"""


class Aluno:
    def __init__(self, codigo, nome, matricula) -> None:
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula

    #Primeira forma para retornar uma string
    def __str__(self) -> str:
        return f'Codigo: {self.codigo}\nNome: {self.nome}\nMatricula: {self.matricula}\n'
    #Segunda forma
    def imprimir(self):
        print(f'\nCodigo: {self.codigo}\nNome: {self.nome}\nMatricula: {self.matricula}')


class AlunoEnsinoMedio(Aluno):
    def __init__(self, codigo, nome, matricula, ano) -> None:
        super().__init__(codigo, nome, matricula)
        self.ano = ano
    
    def imprimir(self):
        super().imprimir() 
        print(f'Ano: {self.ano}')


class AlunoGraduacao(Aluno):
    def __init__(self, codigo, nome, matricula, semestre) -> None:
        super().__init__(codigo, nome, matricula)
        self.semestre = semestre

    def imprimir(self):
        super().imprimir() 
        print(f'Semestre: {self.semestre}')
        

#Instâncias
aluno = Aluno(1,'Guilherme',2021001)
aluno2 = AlunoEnsinoMedio(2, 'Laura', 2021002, 2021)
aluno3 = AlunoGraduacao(3, 'Nei', 2021003, 4)

#Main
aluno.imprimir()
""" metodo __str__ """
#print(aluno)

aluno2.imprimir()
aluno3.imprimir()
