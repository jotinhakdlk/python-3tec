import time
import adivinha
import forca
import forwhile


print("Olá! Deve ter se interessado por jogos no console, não é mesmo?")
print("Escolha o jogo desejado!(Digite o número)")
print("1- Adivinhação 2- Forca 3- 'For ou While?'")

jogoescolhido = int(input("Resposta: "))

if(jogoescolhido == 1):
    print("Entrando no jogo de adivinhação...")
    time.sleep(3)
    adivinha.jogar_adivinhacao()
elif(jogoescolhido == 2):
    print("Entrando no jogo da forca...")
    time.sleep(3)
    forca.jogar_forca()
elif(jogoescolhido == 3):
    print("Entrando no jogo de for ou while...")
    time.sleep(3)
    forwhile.jogar_forwhile()
    