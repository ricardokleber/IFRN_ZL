import  os

class TV:
    def __init__(self):
        self.canal = 1
        self.volume = 1
    
    def mudarCanal(self,canal):
        if canal > 0 and canal < 100:
            self.canal = canal
    
    def aumentarVolume(self):
        if self.volume < 101:
            self.volume += 1

    def diminuirVolume(self):
        if self.volume > 1:
            self.volume -= 1

minhatv = TV()

while True:
    os.system('cls')
    print(f'MinhaTV | Canal: {minhatv.canal} | Volume: {minhatv.volume}')
    print('''
        1) Mudar Canal
        2) Aumentar Volume
        3) Diminuir Volume
        4) Desligar
    ''')

    opcao = int(input('Digite a Opção: '))

    if opcao == 1:
        canal = int(input('Qual Canal Deseja Sintonizar? '))
        minhatv.mudarCanal(canal)
    
    elif opcao == 2:
        minhatv.aumentarVolume()

    elif opcao == 3:
        minhatv.diminuirVolume()

    elif opcao == 4:
        break