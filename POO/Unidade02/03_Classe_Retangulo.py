class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudarValorLados(self, base, altura):
        self.base = base
        self.altura = altura

    def retornarValorLados(self):
        return self.base, self.altura

    def calcularArea(self):
        return self.base * self.altura

    def calcularPerimetro(self):
        return (2 * self.base) + (2 * self.altura)

Base = int(input('digite o valor da base do retângulo: '))
Altura = int(input('digite o valor da altura do retângulo: '))

# Testando a Classe Retangulo (instanciando objeto retangulo_01)

retangulo_01 = Retangulo(Base,Altura)

print('O valor da Área do Retângulo é: ',retangulo_01.calcularArea())
print('O valor do Perímetro do Retângulo é: ',retangulo_01.calcularPerimetro())