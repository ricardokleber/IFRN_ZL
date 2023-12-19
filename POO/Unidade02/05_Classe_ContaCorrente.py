import os

class ContaCorrente:
    def __init__(self, nConta, nomeCliente, saldo=0):
        self.nConta = nConta
        self.nomeCliente = nomeCliente
        self.saldo = float(saldo)
    
    def alterarNome(self, nome):
        self.nomeCliente = nome
    
    def deposito(self, valor):
        self.saldo += valor
    
    def saque(self, valor):
        if self.saldo > valor:
            self.saldo -= valor

conta = int(input('Informe o Número da Conta do Novo Cliente: '))
nome = input('Nome do Novo Cliente: ')
cliente1 = ContaCorrente(conta,nome)

while True:
    os.system('cls')
    print(f'Cliente: {cliente1.nomeCliente} | Conta Corrente: {cliente1.nConta} | Saldo = R$ {cliente1.saldo}')
    print('''
        1) Alterar Nome do Cliente
        2) Fazer Depósito
        3) Fazer Saque
        4) Sair
    ''')

    opcao = int(input('Informe a Opção: '))

    if opcao == 1:
        nome = input('Novo Nome do Cliente: ')
        cliente1.alterarNome(nome)

    elif opcao == 2:
        deposito = float(input('Valor a Depositar: '))
        cliente1.deposito(deposito)

    elif opcao == 3:
        saque = float(input('Valor a Sacar: '))
        cliente1.saque(saque)

    elif opcao == 4:
        break
