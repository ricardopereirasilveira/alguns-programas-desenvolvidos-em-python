from classes.cliente import Cliente

class pessoaFisica(Cliente):
  """Está classe será importada no 'main', com isto, ela será a responsável por chamar todos os métodos para inicialização da Classe.
  """
  def __init__(self, nome: str, idade: int, tipoConta: str, conta: str, nAgencia: int, nConta: int, banco: str, limite=100) -> None:
    super().__init__(nome, idade, tipoConta, conta, nAgencia, nConta, banco)
    self.limite = limite
    self.numeroTransferencia = 0

  def sacar(self, valor: float):
    """Este método é responsável por sacar o dinheiro do cliente! É necessário fazer uma autenticação no BANCO para verificar se o banco corresponde. O saldo é retirado conforme solicitado além do LIMITE disponível para CHEQUE ESPECIAL. O primeiro saque é gratuito, após o primeiro, existe uma taxa de R$1,00 por saque. 
    """
    if self.banco == '341':
      if self._saldo > valor:
        self._saldo -= valor
      elif self._saldo < valor:
        if (self._saldo + self.limite) > valor:
          self._saldo -= valor
        else:
          print('Saldo e Limite indispóniveis! ')
    else:
      print(f'Você está tentando sacar de um banco incorreto! Use o seu banco {self.banco}')

  
  def transferir(self, outroCliente: Cliente, agencia: int, conta: int, valorTransferencia: float):
    """Este método aqui é responsável por transferir o dinheiro entre contas usando as proprias instancias de classes. 
    """
    if self.banco == '341':
      if (self._saldo + self.limite) < valorTransferencia:
        print(f'seu saldo é de R$ {self._saldo}, você não pode transferir o valor de R$ {valorTransferencia}')
      else:
        self.numeroTransferencia += 1
        if self.numeroTransferencia > 1:
          self._saldo -= valorTransferencia
          self._saldo -= 1.00
          print(f'Agora seu saldo é de {self._saldo}')
          outroCliente._saldo += valorTransferencia
          print(f'Você transferiu R$ {valorTransferencia} para {outroCliente._nome}. Esta é sua {self.numeroTransferencia} transferência. Foi cobrado o valor de R$ 1.00 pela transferência. ')
        else:
          self._saldo -= valorTransferencia
          print(f'Agora seu saldo é de {self._saldo}')
          outroCliente._saldo += valorTransferencia
          print(f'Você transferiu R$ {valorTransferencia} para {outroCliente._nome}. Esta é sua {self.numeroTransferencia} transferência. Então nada foi cobrado! ')
    else:
      print('este banco não é o seu banco de origem')