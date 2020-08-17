from classes.agenda import Phonebook

class theFunctions(Phonebook):
  def ligar(self, contact:str):
    for k, v in self.agenda.items():
      if (contact in k) or (contact in v):
        if self.calling == False:
          print(f'Ligando para {k}, {v}')
          self.calling = True
          self.isCalling = contact
        else:
          theFunctions.chamadaEmEspera(self, k, v)

      elif contact in v:
        pass

  def chamadaEmEspera(self, contact:str, numero:str):
    if self.callWaiting == False:
      print(f'A ligação com {self.isCalling} foi colocada em espera, ligando para {contact}, {numero}...')
      self.callWaiting = True
      self.isCallingWaiting = contact
    elif self.callWaiting == True:
      print(f'Não é possível fazer a ligação, pois já esta em chamada para {self.isCalling} e também com a chamada em espera ativa {self.isCallingWaiting}')

  def desligar (self):
    if (self.calling == False) and (self.callWaiting == False):
      print('Você não pode desligar a chamada, pois não está em uma!')
    elif self.calling == True and self.callWaiting == False:
      print(f'Desligando a chamada com {self.isCalling}... Agora você não está em chamada mais...')
      self.calling = False
      self.isCalling = str
    elif self.calling == True and self.callWaiting == True:
      print(f'Desligando a chamada em espera {self.isCallingWaiting}')
      self.isCallingWaiting = str
      self.callWaiting = False
      return

    
