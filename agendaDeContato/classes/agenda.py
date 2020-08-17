class Phonebook:
  def __init__(self):
    self.agenda = {}
    self.calling = False
    self.isCalling = str
    self.callWaiting = False
    self.isCallingWaiting = str

  def addContact(self, nome:str, telefone:str):
    self.agenda[f'{nome}'] = f'{telefone}'

  def delContact(self, nome:str):
    pass

  def checkAllContacts(self):
    for nome, telefone in self.agenda.items():
      print(f'nome: {nome} | telefone: {telefone}')
  
  def checkContact(self, contact:str):
    validating = True
    for k,v in self.agenda.items():
      if k == contact:
        print(f'nome: {contact} | telefone: {self.agenda[k]}')
        validating = False
        break
      elif v == contact:
        print(f'nome: {k} | telefone: {v}')
        validating = False
        break
      else:
        pass

    if validating == True:
      print(f'Contato {contact} não existe')
