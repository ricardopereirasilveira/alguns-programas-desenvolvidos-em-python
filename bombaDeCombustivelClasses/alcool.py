class Alcool:
    quantidadeDeAlcool = 0
    valorDoAlcool = 1.00

    def atualizarQuantidade(self, valor):
        Alcool.quantidadeDeAlcool += valor
        return

    def atualizarValorAlcool(self, valor):
        Alcool.valorDoAlcool = valor
        print(f'O valor do álcool foi atualizado para R$ {Alcool.valorDoAlcool}.')


class AbastecerPorValor(Alcool):
    def __init__(self, valor):
        quantidadeLitros = valor / Alcool.valorDoAlcool
        if Alcool.quantidadeDeAlcool < quantidadeLitros:
            print(f'Desculpe, não existe a quantidade de litro validas para adicionar o carro!')
            print(f'O Taque só tem disponível {Alcool.quantidadeDeAlcool} Litro(s)')
        else:
            Alcool.quantidadeDeAlcool = (Alcool.quantidadeDeAlcool - quantidadeLitros)
            print(
                f'Carro abastecido com sucesso. Valor da compra {valor}. A quantidade de litros abastecido(s) foram {quantidadeLitros} litro(s)! Obrigado.')


class AbastecerPorLitro(Alcool):
    def __init__(self, litros):
        if Alcool.quantidadeDeAlcool >= litros:
            Alcool.quantidadeDeAlcool -= litros
            print(f'Você abasteu {litros} litros! O total da sua compra deu R$ {litros * Alcool.valorDoAlcool}!')
        else:
            print(f'Não temos esta quantidade de Álcool no taque! Nossa quantidade é de {Alcool.quantidadeDeAlcool}')


class quantidadeAlcoolNoTanque(Alcool):
    def quantidade(self):
        return float(Alcool().quantidadeDeAlcool)


class atualizarValorAlcool(Alcool):
    def definirValor(self, novoValor):
        Alcool().atualizarValorAlcool(novoValor)


class inserirCombustivelNoTaque(Alcool):
    def adicionar(self, valor):
        Alcool().atualizarQuantidade(valor)
