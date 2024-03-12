'''

Recriação do jogo
    Pedra
     Papel
      Tesoura

              '''
import random  #biblioteca que implementa a geração de números pseudoaleatórios

resposta = int(input('''A decisão é sua! Pedra, Papel ou Tesoura.

[1] Pedra
[2] Papel
[3] Tesoura
 
Qual a sua escolha: '''))
computador = random.randint(1,3)

if computador == 1:                                   # PEDRA
    print('O computador escolheu: Pedra')
    if resposta == 1:
        print("Empate!")
    elif resposta == 2:
        print("Jogador perdeu")
    elif resposta == 3:
        print("Computador venceu")
    else:
        print("Digite um número")

elif computador == 2:                                # PAPEL
    print('O computador escolheu: Papel')
    if resposta == 1:
        print("Computador venceu")
    elif resposta == 2:
        print("Empate!")
    elif resposta == 3:
        print("Jogador venceu")
    else:
        print("Digite um número")
elif computador == 3:                               # TESOURA
    print('O computador escolheu: Tesoura')
    if resposta == 1:
        print("Jogador venceu")  
    elif resposta == 2:
        print("Computador venceu")                     
    elif resposta == 3:
        print("Empate!")                               
    else:
        print("Digite um número")
else:
    print("Opção incorreta")
