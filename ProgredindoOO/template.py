class Programas:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._curtir = 0
    
    @property
    def valor_curtir(self):
        return self._curtir
    
    @property
    def valor_nome(self):
        return self._nome
    
    def curtida(self):
        self._curtir += 1

class Filmes(Programas):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

class Series(Programas):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas



BreakingBad = Series("Breaking Bad", 2008, 5)
BeeMovie = Filmes("Bee Movie", 2007, 91)

filmes_series = [BreakingBad, BeeMovie]

BreakingBad.curtida()

for programas in filmes_series:
    detalhe = programas.duracao if hasattr(programas, 'duracao')
    print(f"")
