class Conta:
    def __init__(self, numero, titular, saldo, limite = 1000.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

## Crie uma classe que represente um vídeo com os atributos título, duração e views

class Video:
    def __init__(self, titulo, duracao, views):
        self.titulo = titulo
        self.duracao = duracao
        self.views = views
## Como poderia ser criada uma classe que represente o objeto livro = Livro(titulo, autor, data_publicacao)?

class Livro:
    def __init__(self, titulo, autor, data_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.data_publicacao = data_publicacao

livro = Livro("Hobit", "Tolken", 1980)