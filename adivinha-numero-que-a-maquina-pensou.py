# Crie um programa que escolha aleatoriamente um número para adivinhar e, em seguida, o usuário terá algumas chances de adivinhar o número corretamente.
# Em cada tentativa incorreta, o computador indicará que o número é maior ou menor do que aquele que você adivinhou.


import random

print('Aguarde... A maquina está pensando em um número...')
numeroEscolhido = random.randint(1, 100)
# print(numeroEscolhido)
numeroDigitado = int(input("Que número a maquina pensou? : "))


while numeroDigitado != numeroEscolhido:
    print('Você digitou o número errado!')
    if numeroDigitado < numeroEscolhido:
        print('Você precisa digitar um número maior!')

    else:
        print('Você precisa digitar um número menor')

    numeroDigitado = int(input("Tente novamente...: "))


print(f'Parabéns, você digitou o número {numeroEscolhido}, este é o número pensado pela maquina!')
