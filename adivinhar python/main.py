import random as rd
print("_________________________________")
print("Seja bem vindo ao adivinha python!")
print("_________________________________")

n_secreto = rd.randrange(1, 101)
n_tentativas = 5
rodada = 1
print(n_secreto)
for n_tentativas in range(1, n_tentativas + 1):
    print(f"rodada {rodada}/{n_tentativas}")
    entrada = int(input("digite um número entre 1 e 100: "))
    acerto = entrada == n_secreto
    chutemaior = entrada > n_secreto
    chutemenor = entrada < n_secreto

    if(entrada > 100 or entrada < 1):
        print("Tu digitou um valor inválido doido")
        continue

    print(f"Você digitou o número: {entrada}")

    if(acerto):
        print("pabens, asserto")
        break
    else:
        if(chutemaior):
            print("o número secreto é menor que seu chute")
        if(chutemenor):
            print("o número secreto é maior que seu chute")

    rodada = rodada + 1
print("It's over, sobrou nada pro beta")