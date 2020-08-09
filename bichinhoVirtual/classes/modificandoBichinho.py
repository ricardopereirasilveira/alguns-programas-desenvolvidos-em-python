from classes.meubicho import bichinho

class modificar(bichinho):
    def __init__(self, nome, fome, saude, idade):
        super().__init__(nome, fome, saude, idade)
    
    def modificarNome(self, valor):
        if (self.fome > 1) and (self.saude > 1):
            if self._nome != valor:
                self._nome = valor
                print(f'Você modificou o seu nome para {self._nome}')
                self._fome -= 1
                self.saude -= 1
                self.idade += 1
            else:
                print(f'Você não pode alterar seu nome para {valor} pois este já é seu nome')
        elif (self.fome <= 1) or (self.saude <= 1):
            print(f'O {self._nome} está muito cansado! Não é possível alterar o nome dele agora! Que tal alimentar ele e cuidar da saúde dele?')