import alcool
import gasolina


class Combustivel:
    def __init__(self, combustivel):
        self.combustivel = combustivel
        print(f'A bomba está operando em {self.combustivel}')

        self.alcool = alcool.quantidadeAlcoolNoTanque()
        self.gasolina = gasolina.quantidadeGasolinaNoTaque()
        self.nomeBomba = self.__class__.__name__

    def mudarBombaCombustivel(self):
        if self.combustivel == 'alcool':
            self.__init__(combustivel='gasolina')
            print(f'agora a bomba opera em {self.combustivel}')
            return
        self.__init__(combustivel='alcool')
        print(f'agora a bomba opera em {self.combustivel}')

    def atualizarValorLitro(self, novoValor):
        if self.combustivel == 'alcool':
            alcool.atualizarValorAlcool().definirValor(novoValor)
            return
        gasolina.AtualizarValorGasolina().definirValor(novoValor)

    def quantidadeCombustivel(self):
        if self.combustivel == 'alcool':
            print(f'Existe {self.alcool.quantidade()} litro(s) no tanque de {self.combustivel}.')
            return
        print(f'Existe {self.gasolina.quantidade()} litro(s) no taque de {self.combustivel}')

    def adicionarCombustivel(self, quantidade):
        if self.combustivel == 'alcool':
            alcool.inserirCombustivelNoTaque().adicionar(quantidade)
            print(f'Foi adicionado {quantidade} litro(s) no tanque de {self.combustivel}')
            return self.combustivel
        gasolina.inserirCombustivelNoTaque().adicionar(quantidade)
        print(f'Foi adicionado {quantidade} litro(s) no tanque de {self.combustivel}')
        return self.combustivel

    def abastecerPorValor(self, valor):
        if self.combustivel == 'alcool':
            alcool.AbastecerPorValor(valor)
            return
        gasolina.AbastecerPorValor(valor)

    def abastecerPorLitros(self, litros):
        if self.combustivel == 'alcool':
            alcool.AbastecerPorLitro(litros)
            return
        gasolina.AbastecerPorLitro(litros)