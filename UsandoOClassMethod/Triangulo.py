from random import randint


class triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.tamanho1 = ladoA
        self.tamanho2 = ladoB
        self.tamanho3 = ladoC
        # print(self.tamanho1, self.tamanho2, self.tamanho3)

    # Aqui nós verificaremos se o valor fornecido pelo usuário retorna umr retângulo.
    def verificando(self):
        if self.tamanho1 == self.tamanho2 and self.tamanho3 == self.tamanho1:
            print(f'O Triângulo com as medidas de {self.tamanho1} x {self.tamanho2} x {self.tamanho3} é um Equilátero!')

    # Método de Classe para criar um retângulo Equilátero
    @classmethod
    def criarEquilateroManual(cls, tamanho):
        return cls(tamanho, tamanho, tamanho)

    @classmethod
    def criarEscalenoAutomatico(cls, tamanhoMinino, tamanhoMaximo):
        tamanho1 = randint(tamanhoMinino, tamanhoMaximo)
        tamanho2 = randint(tamanhoMinino, tamanhoMaximo)
        tamanho3 = randint(tamanhoMinino, tamanhoMaximo)
        while True:
            if tamanho1 == tamanho2 and tamanho3 == tamanho1:
                return cls(tamanho1, tamanho2, tamanho3)
            else:
                tamanho1 = randint(tamanhoMinino, tamanhoMaximo)
                tamanho2 = randint(tamanhoMinino, tamanhoMaximo)
                tamanho3 = randint(tamanhoMinino, tamanhoMaximo)
                # print('ainda não')


