print("********************************************")
print("  Bem-vindo ao programa FOR ou WHILE! :P")
print("********************************************")


print("Você prefere utilizar while ou for?(resposta toda em minúscula)")
resposta = input("Resposta:")
n_inicial = 1
checa_terminou = False

if(resposta == "while"):
    print(f"então utilizarei {resposta} para contar até um número, qual número seria mais do seu agrado? (cuidado com números muito grandes ai bixo, o pc tbm sofre)")
    numero_while = int(input("Número: "))
    print(f"Ok! Contando até {numero_while}...")
    while(checa_terminou == False):
        print(n_inicial)
        n_inicial = n_inicial + 1
        if(n_inicial == numero_while + 1):
            checa_terminou = True
    print("Pronto!! Até mais!")

if(resposta == "for"):
    print(f"Beleza! Então vou usar {resposta} para contar até um número, que número você deseja? (números altos tem risco de explosão da máquina)")
    numero_for = int(input("Número: "))
    print(f"Tranquilo! Contando até {numero_for} utilizando for...")
    for n_inicial in range (1, numero_for + 1):
        while(checa_terminou == False):
            print(n_inicial)
            print("Adiciono mais um?")
            n_inicial = n_inicial + 1
            if(n_inicial == numero_for + 1):
                checa_terminou = True
    print("Não! Até a próxima!")

else:
    print("você digitou uma resposta inválida! Reinicie o programa caso queira tentar novamente.")





