class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    ## Declaração dos métodos (funções)
    def extrato(self):
        print(f"Saldo {self.saldo} do titular {self.titular}")
    
    def depositar(self, valor):
        if(valor < 0):
            print("Não é possível depositar um valor negativo")
        else:
            self.saldo += valor

    def sacar(self, valor):
        if(self.saldo < valor):
            print(f"Não é possível sacar este valor ({valor})")
        else:
            self.saldo -= valor

    def extrato(self):
        print(f'Seu saldo é {self.saldo}')