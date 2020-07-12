class Gasolina:
  quantidadeDeGasolina = 0
  valorDaGasolina = 1.00


class quantidadeGasolinaNoTaque(Gasolina):
  def quantidade(self): 
    return float(super().quantidadeDeGasolina)


class inserirCombustivelNoTaque(Gasolina):
  def adicionar(self, valor): 
    Gasolina.quantidadeDeGasolina += valor
    return self.quantidadeDeGasolina


class AbastecerPorValor(Gasolina):
  def __init__(self, valor):
    quantidadeLitros = (valor / self.valorDaGasolina)
    if Gasolina.quantidadeDeGasolina < quantidadeLitros:
      print(f'Desculpe, não existe a quantidade de litro validas para adicionar o carro!')
      print(f'O Taque só tem disponível {Gasolina.quantidadeDeGasolina} Litro(s)')
    else:
      Gasolina.quantidadeDeGasolina = (Gasolina.quantidadeDeGasolina - quantidadeLitros)
      print(f'Carro abastecido com sucesso. Valor da compra {valor}. A quantidade de litros abastecido(s) foram {quantidadeLitros} litro(s)! Obrigado.')


class AtualizarValorGasolina(Gasolina):
  def definirValor(self, valor):
    Gasolina.valorDaGasolina = valor
    print(f'O valor da gasolina agora é: {Gasolina.valorDaGasolina}')


class AbastecerPorLitro(Gasolina):
  def __init__(self, litros):
    if Gasolina.quantidadeDeGasolina >= litros:
      Gasolina.quantidadeDeGasolina -= litros
      print(f'Você abasteu {litros} litros! O total da sua compra deu R$ {litros * Gasolina.valorDaGasolina}!')
    else:
      print(f'Não temos esta quantidade de Álcool no taque! Nossa quantidade é de {Gasolina.quantidadeDeGasolina}')
