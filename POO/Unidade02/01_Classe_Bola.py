class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self,cor):
        self.cor = cor

    def mostraCor(self):
        print('A cor da bola é: ', self.cor)

# Testando a Classe Bola (instanciando objeto bola_01)

bola_01 = Bola('Azul', 10, 'plástico')
bola_01.trocaCor('Verde')
bola_01.mostraCor()