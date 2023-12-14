class Quadrado:
    def __init__(self, tamanhoLado):
        self.tamanhoLado = tamanhoLado

    def mudarValorLado(self, tamanhoLado):
        self.tamanhoLado = tamanhoLado

    def retornarValorLado(self):
        return self.tamanhoLado

    def calcularArea(self):
        return self.tamanhoLado * self.tamanhoLado

# Testando a Classe Quadrado (instanciando objeto quadrado_01)
    
quadrado_01 = Quadrado(2)
quadrado_01.mudarValorLado(6)
print('O valor do Lado do Quadrado é: ', quadrado_01.retornarValorLado())
print('O valor da Área do Quadrado é: ', quadrado_01.calcularArea())