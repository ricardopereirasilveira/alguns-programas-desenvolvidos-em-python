from classes.pessoa import Pessoa
from abc import ABC, abstractmethod

class Cliente(Pessoa, ABC):
  """Classe que inicia os parmetros
    
  Nesta classe estamos cadastrando os clientes. É necessário informar se o cliente é "PJ" ou "PF". Posteriormente será informado se o cliente está abrindo uma conta PJ ou PF. É necessário informar o número da conta e a agência manualmente. Ainda não foi criado o cadastro de conta automáticamente.
  """

  def __init__(self, nome: str, idade: int, tipoConta: str, conta: str, nAgencia: int, nConta: int, banco: str):
    """
    :nome - STR: Nome completo do dono da conta
    :idade - INT: - Idade do dono da conta
    :tipoConta - STR: - Aqui informamos se é uma pessoa física ou uma pessoa júrifica. Existem apenas dois padrões "PF" ou "PJ"
    :conta - STR: - Aqui informamos se a conta é "PF" ou "PJ"
    :nAgencia - INT: Aqui informaremos o número da agência, que deve ser inserido manualmente pois não temos o cadastro de agência automática ainda.
    :nConta - INT: - Aqui informaremos o número da conta, que deve ser inserido manualmente pois não temos o cadstro de conta automática ainda.
    :banco - STR: - Informe o nome do banco vigente para futura autenticação. 
    """
    super().__init__(nome, idade, tipoConta, banco)
    self.conta = conta
    self.nAgencia = nAgencia
    self.nConta = nConta
    self._saldo = 0


  @property
  def conta(self):
    return self._conta
  @conta.setter
  def conta(self, valorConta):
    if valorConta == 'PF' and self._tipoConta == 'PJ':
      raise ValueError('Não é possível abrir uma conta PF para uma pessoa PJ')
    elif valorConta == 'PJ' and self._tipoConta == 'PF':
      raise ValueError('Não é possível abrir uma conta PJ para uma pessoa PF')
    self._conta = valorConta
  
  
  @property
  def nConta(self):
    return self._nConta
  @nConta.setter
  def nConta(self, valorConta):
    if not isinstance(valorConta, int):
      raise ValueError('O número da conta esta incorreto')
    self._nConta = valorConta

  def depositar(self, valor):
    """ Este é o método que deposita o valor na conta do cliente.
    
    :valor - FLOAT: - Valor a ser depositar, incrementa o SALDO do cliente total.
    """
    print(f'Você depositou {valor}')
    self._saldo += valor
    print(f'Seu saldo é de {self._saldo}')
  
  def consultarSaldo(self):
    """Aqui é possível consultar o saldo do cliente. Retorna um print com o saldo total do cliente até o momento. 
    """
    print(self._saldo)
  
  @abstractmethod
  def sacar(self, valorSaque):
    """Este é um método Abstrato. Ele não será usado nesta classe aqui, pois quem deve usar ele na verdade são as classes filhas (Pessoa física e Pessoa Jurídica.). Este método será responsável por sacar o dinheiro do cliente da conta.
    """
    pass
  
  @abstractmethod
  def transferir(self, agencia, conta, valor):
    """Este é um método Abstrato. Ele não será usado nesta classe aqui, pois quem será responsável por ela serão as classes filhas (Pessoa física e Pessoa Jurídica). Este método será o responsável por transferir o diheiro entre duas instâncias. 
    """
    pass
  
