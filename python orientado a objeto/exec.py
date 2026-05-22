from conta import Conta

conta = Conta(321, "João", 55.0, 5000.0)
conta2 = Conta(555, "Fulano", 100.0, 1000.0)

conta.sacar(100)
conta.extrato()