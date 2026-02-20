print("_________________________________")
print("Seja bem vindo ao adivinha python!")
print("_________________________________")

n_secreto = 50
n_tentativas = 5
rodada = 1

for n_tentativas in range(1, n_tentativas + 1):
    print(f"rodada {rodada}/{n_tentativas}")
    entrada = int(input("digite um valor aleatório: "))
    acerto = entrada == n_secreto
    chutemaior = entrada > n_secreto
    chutemenor = entrada < n_secreto

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