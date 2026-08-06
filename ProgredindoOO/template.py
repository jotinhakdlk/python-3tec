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
    
    def __str__(self):
        return f"{self.valor_nome} - {self.ano} - {self._curtir}"


class Filmes(Programas):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self.valor_nome} - {self.ano} - {self.duracao} mins - {self._curtir} curtidas"

class Series(Programas):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self.valor_nome} - {self.ano} - {self.temporadas} temporadas - {self._curtir} curtidas"

class Playlist:
    def __init__(self, nomePl, elementos):
        self.nomePl = nomePl
        self._elementos = elementos

        @property
        def listagem(self):
            return self._elementos
        
        @property
        def tamanho(self):
            return len(self._elementos)
    


#Series
BreakingBad = Series("Breaking Bad", 2008, 5)
CobraKai = Series("CobraKai", 2018, 6)

##Filmes
BeeMovie = Filmes("Bee Movie", 2007, 91)
Minecraft = Filmes("Um Filme Minecraft", 2025, 101)

#Curtidas
BreakingBad.curtida()
CobraKai.curtida()
CobraKai.curtida()
Minecraft.curtida()
Minecraft.curtida()
Minecraft.curtida()

filmes_series = [BreakingBad, CobraKai, BeeMovie, Minecraft]
plFim_de_semana = Playlist("Fim de Semana", filmes_series)

print(f"Tamanho da playlist: {len(plFim_de_semana)}")
print(f"Está na lista? {BeeMovie in plFim_de_semana}")

for programas in plFim_de_semana._elementos:
        print(programas)

## nomePl = nome da playlist
