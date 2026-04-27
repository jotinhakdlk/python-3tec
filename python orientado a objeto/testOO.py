#NumConta = 8765456
#titular = 'Fulano'
#saldo = 1557.90
#limite = 10000

#contas = {'NumConta': NumConta, 'titular': titular, 'saldo': saldo, 'limite': limite
#}

def criar_conta(numero, titular, saldo ,limite):
    conta = {'numero':numero, 'titular':titular, 'saldo':saldo, 'limite':limite}
    return conta

conta = criar_conta(345, 'João', 200.0, 1000.0)

def depositar(conta, valor):
    conta['saldo'] += valor

def sacar(conta, valor):
    conta['saldo'] -= valor

def extrato(conta):
    print(f'Seu saldo é {conta['saldo']}')

sacar(conta, 1000)
extrato(conta)