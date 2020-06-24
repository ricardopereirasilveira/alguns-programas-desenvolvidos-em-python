# o simulador de rolar dados imitará a experiência de rolar um dado.
# Irá gerar um número aleatório e o usuário poderá jogar repetidamente para obter um número do utilitário de dados que o usuário corta para sair do programa
# Insira a opção de placar também, alem da possibilidade de sair do jogo.

import random
import time

vitoriasMaquina = 0
vitoriasJogador = 0
empate = 0

while True:
    print('''Digite uma opção
    [1] Jogar
    [2] Ver resultado parcial
    [3] Sair
    ''')
    opcoes = int(input("Digite a opção desejada: "))

    if opcoes == 1:
        dadoMaquina = random.randint(1, 6)
        print('Aguarde, a maquina esta jogando o dado...')
        time.sleep(1)
        print(f'O dado da maquina deu: {dadoMaquina}')

        time.sleep(1)
        # apertarEnter = input('Aperte o enter para rolar seu dado...')
        print('Aguarde, o seu dado esta rolando...')
        time.sleep(1)

        dadoJogador = random.randint(1, 6)
        print(f'O seu dado caiu no {dadoJogador}')

        if dadoJogador == dadoMaquina:
            print('Vocês empataram..')
            empate += 1

        elif dadoJogador > dadoMaquina:
            print('Você ganhou, parabéns...')
            vitoriasJogador += 1

        else:
            print('A maquina ganhou...')
            vitoriasMaquina +=1

    elif opcoes == 2:
        print(f'Placar Parcial: Maquina {vitoriasMaquina} - Jogador {vitoriasJogador} - Empate - {empate}')
        if vitoriasMaquina > vitoriasJogador:
            print('Vamos lá, você precisa de mais sorte, a maquina está ganhando...\n\n\n')\

        elif vitoriasMaquina == vitoriasJogador:
            print('Estamos empatados, vamos jogar para ganhar...\n\n\n')

        else:
            print('É isso ai, continue assim, você está na frente...\n\n\n')

    else:
        print(f'Placar Final: Maquina {vitoriasMaquina} - Jogador {vitoriasJogador} - Empate - {empate}')
        if vitoriasJogador > vitoriasMaquina:
            print('Parabéns, você venceu a maquina ;)\n\n\n')

        elif vitoriasMaquina == vitoriasJogador:
            print('terminamos empatados, foi por pouco em ;)')

        else:
            print('Infelizmente a maquina se deu melhor nesta vez, mais sorte na próxima jogatina :D')
        break

