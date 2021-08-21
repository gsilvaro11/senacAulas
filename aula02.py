class Retangulo:
    def __init__(self, altura = 0, largura = 0):
        self._altura = altura
        self._largura = largura       

    def calculaArea(self):
        try:
            return f'Retangulo: {int(self._altura) * int(self._largura)}' 
        except:
            return 'ERRO'

    def __str__(self) -> str:
        return f'Altura: {self._altura}\nLargura: {self._largura}'
        
retangulo = Retangulo(10,2)
print(retangulo.calculaArea())  
print(retangulo) 

