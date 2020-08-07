class Pessoa:
  def __init__(self, nome: str, idade: int, tipoConta: str, banco: str) -> None:
    self.nome = nome
    self.idade = idade
    self.tipoConta = tipoConta
    self.banco = banco


  @property
  def nome(self):
    return self._nome
  @nome.setter
  def nome(self, novoNome):
    if not isinstance(novoNome, str):
      raise ValueError('O nome está incorreto!')
    self._nome = novoNome


  @property
  def idade(self):
    return self._idade
  @idade.setter
  def idade(self, novaIdade):
    idade = int(novaIdade)
    if not isinstance(idade, int):
      raise ValueError('O valor de idade está incorreto')
    self._idade = idade
  

  @property
  def tipoConta(self):
    return self._tipoConta
  @tipoConta.setter
  def tipoConta(self, valorConta):
    if valorConta == 'PF' or valorConta == 'PJ':
      self._tipoConta = valorConta
    else:
      raise ValueError('A conta deve PF ou PJ')