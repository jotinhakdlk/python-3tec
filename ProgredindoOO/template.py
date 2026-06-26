class Filmes:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__curtir = 0

    def curtida(self):
        self.curtir += 1
 
class Series:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome
        self.ano = ano
        self.temporadas = temporadas
        self.__curtir = 0

    @property
    def valor_curtir(self):
        return self.__curtir
    
    @property
    def valor_nome(self):
        return self.__nome

    def curtida(self):
        self.curtir += 1

BreakingBad = Series("Breaking Bad", 2008, 5)
print(f'Nome: {BreakingBad.nome} - Ano: {BreakingBad.ano} - Temporadas: {BreakingBad.temporadas}')
BeeMovie = Filmes("Bee Movie", 2007, 91)
print(f'Nome: {BeeMovie.nome} - Ano: {BeeMovie.ano} - Minutos: {BeeMovie.duracao}')

BreakingBad.curtida()
print(BreakingBad.curtir)