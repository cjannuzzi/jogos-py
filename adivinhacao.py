import random

def jogar ():
    print("********************************")
    print("Bem vindo ao jogo de advinhação!")
    print("********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos =1000
    print(numero_secreto)

    print("Qual o nível de dificuldade?")
    print(" | (1) Fácil   |\n | (2) Normal  |\n | (3) Difícil |\n")

    nivel = int(input("Defina o nível: "))

    if (nivel==1):
        total_de_tentativas = 20
    elif (nivel==2):
        total_de_tentativas =10
    elif (nivel==3):
        total_de_tentativas =5
    else:
        print("***Digite uma opção válida!***")

    for rodada in range(1, total_de_tentativas+1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou", chute)

        if(chute <1 or chute >100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute) #40-20 = 20 pts perdidos
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")
if(__name__=="__main__"):
    jogar()