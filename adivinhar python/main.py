import random as rd
print("_________________________________")
print("Seja bem vindo ao adivinha python!")
print("_________________________________")

n_secreto = rd.randrange(1, 101)
n_tentativas = 0
rodada = 1
pontos = 1000

print("Escolha o nível da dificuldade!")
print("/n 1-Fácil 2-Médio 3-Difícil 4-Extremo 5-Aleatório")

nivel = int(input("Defina o nível:"))

if(nivel == 1):
    n_tentativas = 12
elif(nivel == 2):
    n_tentativas = 7
elif(nivel == 3):
    n_tentativas = 5
elif(nivel == 4):
    n_tentativas = 1
else:
    aleatorio = rd.randrange(1, 6)
    nivel = aleatorio

for rodada in range(1, n_tentativas + 1):
    print(f"Você está na {rodada} de {n_tentativas}")
    entrada = int(input("digite um número entre 1 e 100: "))


    if(entrada > 100 or entrada < 1):
        print("Tu digitou um valor inválido doido")
        rodada = rodada + 1
        continue

    print(f"Você digitou o número: {entrada}")
    acerto = entrada == n_secreto
    chutemaior = entrada > n_secreto
    chutemenor = entrada < n_secreto
    valor_aceitavel = True


    if(acerto):
        print(f"pabens, asserto! Você fez {pontos} pontos!")
        break
    else:
        if(chutemaior):
            print("o número secreto é menor que seu chute")
        if(chutemenor):
            print("o número secreto é maior que seu chute")
    pontos_perdidos = abs(n_secreto - entrada)
    pontos = pontos - pontos_perdidos
    rodada = rodada + 1
print("It's over, sobrou nada pro beta")


