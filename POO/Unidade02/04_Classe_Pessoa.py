from os import system

class Pessoa:
    def __init__(self, nome="pessoa", idade=0, peso=0.0, altura=0.0):
        self.nome = nome
        self.idade = int(idade)
        self.peso = float(peso)
        self.altura = float(altura)

    def envelhecer(self, anos):
        if self.idade <= 21:
            if self.idade+anos <= 21:
                self.altura += 0.5 * anos
            else:
                aumenta = 21 - self.idade
                self.altura += 0.5 * aumenta
        self.idade += anos

    def engordar(self, kg):
        self.peso += kg

    def emagrecer(self, kg):
        self.peso -= kg

    def crescer(self, cm):
        self.altura += cm

nome = input('Qual o nome da Pessoa? ')
idade = int(input(f'Qual a idade de {nome}? '))
peso = float(input(f'Qual o peso de {nome} em Kg? '))
altura = float(input(f'Qual a altura de {nome} em cm? '))
pessoa1 = Pessoa(nome,idade,peso,altura)

while True:
    system('clear')
    print(f'Dados da Pessoa: Nome: {pessoa1.nome} | Idade: {pessoa1.idade} anos | Peso: {pessoa1.peso} Kg | Altura: {pessoa1.altura} cm')
    print("""
    1) Envelhecer
    2) Engordar
    3) Emagrecer
    4) Crescer
    5) Finalizar
    """)

    opcao = int(input('Digite a opção: '))

    if opcao == 1:
        anos = int(input(f'{pessoa1.nome} envelheceu quantos anos? '))
        pessoa1.envelhecer(anos)
    
    elif opcao == 2:
        peso = float(input(f'{pessoa1.nome} engordou quantos quilos? '))
        pessoa1.engordar(peso)

    elif opcao == 3:
        peso = float(input(f'{pessoa1.nome} emagreceu quantos quilos? '))
        pessoa1.emagrecer(peso)

    elif opcao == 4:
        crescimento = float(input(f'{pessoa1.nome} cresceu quantos cm? '))
        pessoa1.crescer(crescimento)
    elif opcao == 5:
        break