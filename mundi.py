"""
mapa -> Grafo
    paises
        estados 
            
"""

class Estado:
    def __init__(self, nome:str, tamanho:int):
        self.nome = nome
        self.tamanho = tamanho

class Pais:
    def __init__(self, nome:str, bandeira:str):
        self.nome = nome
        self.bandeira = bandeira
        self.estados = []
    
    def adiciona_estado(self, estado: Estado):
        self.estados.append(estado)

    def lista_estado(self):
        print(f"{self.nome} {self.bandeira}\n")
        for estado in self.estados:
            print(f"Estado: {estado.nome} - Tamanho: {estado.tamanho}")

class Mapa:
    brasil = Pais("Brasil", "🏳️‍🌈")
    brasil.adiciona_estado(Estado("SP",1000))
    brasil.adiciona_estado(Estado("MG",800))
    brasil.adiciona_estado(Estado("RJ",850))
    brasil.adiciona_estado(Estado("Sp",1000))
    brasil.adiciona_estado(Estado("Sp",1000))

    argentina = Pais("Argentina", "🏳️‍🌈")
    brasil.adiciona_estado(Estado("SP",1000))

mapa = Mapa()
mapa.brasil.lista_estado()