class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    ## Declaração dos métodos (funções)
    def extrato(self):
        print(f"Saldo {self.__saldo} do titular {self.__titular}")
    
    def depositar(self, valor):
        if(valor < 0):
            print("Não é possível depositar um valor negativo")
        else:
            self.__saldo += valor

    def sacar(self, valor):
        if(self.__saldo < valor):
            print(f"Não é possível sacar este valor ({valor})")
        else:
            self.__saldo -= valor

    def extrato(self):
        print(f'Seu saldo é {self.__saldo}')

    def transferir(self, valor, destino):
        if(self.__saldo < valor) or (valor < 0):
            print("Não é possível realizar a transferência")
        else:
            self.sacar(valor)
            destino.depositar(valor)
    
## Método para retornar apenas valores das propriedades    

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite

## Métodos para manipular os valores das propriedades
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
    
