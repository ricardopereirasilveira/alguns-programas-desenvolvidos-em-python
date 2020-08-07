class meuFuncionario:
  def __init__(self, nome: str, salario: float) -> None:
    self.nome = nome
    self.salario = salario
  
  def mostrarFuncionario(self) -> None:
    print(f'Este é o funcionário {self.nome} que recebe {round(self.salario, 2)}')
  
  def aumentarSalario(self, porcentagem: float) -> float:
    if porcentagem >= 1:
      aumento = (porcentagem * 100) / self.salario
      self.salario += aumento
    else:
      raise ValueError('O aumento de salário não pode ser menor que 1.')