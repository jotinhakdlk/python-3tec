class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_branco = '001'

    ## Declaração dos métodos (funções)
    def extrato(self):
        print(f"Saldo {self.__saldo} do titular {self.__titular}")
    
    def depositar(self, valor):
        if(valor <= 0):
            print("Não é possível depositar um valor negativo")
        else:
            self.__saldo += valor
    
    def saque_permitido(self, valor_saque):
        valor_disponivel_saque = self.__saldo + self.__limite
        return valor_saque <= valor_disponivel_saque

    def sacar(self, valor):
        if(self.saque_permitido(valor)):
            self.__saldo -= valor
        else:
            print(f"Não é possível sacar este valor ({valor})")

    def extrato(self):
        print(f'Seu saldo é {self.__saldo}')
        if(self.__saldo < 0):
            print('Cuidado seu saldo está negativo!')

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
    
    @staticmethod
    def codigo_banco():
        return '001'

## Métodos para manipular os valores das propriedades
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
    
