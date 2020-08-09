from classes.modificandoBichinho import modificar

class interagir(modificar):
    def __init__(self, nome, fome, saude, idade):
        super().__init__(nome, fome, saude, idade)
    
    def brincar(self, objeto):
        if self.comendo == False:
            if (self.fome > 2) and (self.saude > 2):
                if self.brincando == False:
                    print(f'Agora você está bricando de {objeto} com ele')
                    self._fome -= 2
                    self.saude -= 2
                    self.idade += 1
                    self.brincando = True
                else:
                    print(f'Não é possível brincar com o {self._nome}, pois ele já está brincando.')
                    self._fome -= 2
                    self.saude -= 2
                    self.idade += 1
            else:
                if self._fome <= 2 and self.saude <= 2:
                    print('O seu bichinho virtual está com fome e com a saúde debilitada! Ajude-o a se curar.')
                elif self._fome <= 2 and self.saude > 2:
                    print('O seu bichinho virtual está com fome! Que tal alimentar ele para poder brincar ?')
                elif self._fome > 2 and self.saude <= 2:
                    print('O seu bichinho virtual está com a saúde baixa! Que tal cuidar da saúde dele?')
                else:
                    print('Algo deu errado!')
        else:
            print(f'Nãe é possível brincar enquanto está comendo!')
            self._fome -= 1
            self.saude -= 1
            self.idade += 1
    
    def pararDeBrincar(self):
        if self.brincando == True:
            print(f'Agora o {self._nome} parou de brincar!')
            self.brincando = False
        else:
            print(f'O {self._nome} já não estava brincando mais!')

    
    def comer(self, alimento):
        if self.brincando == False:
            if self._fome >= 9:
                print('Você não pode alimentar ele mais, ele não aguenta mais comer')
                self.comendo = False
            else:
                if self.comendo == True:
                    print('Você não pode alimentar ele duas vezes seguida. Ele já está comendo')
                else:
                    print(f'Agora o {self._nome} está comendo {alimento}')
                    self.comendo = True
                    self._fome =+ 2
        else:
            print(f'Você não pode comer enquanto brinca!')
            self._fome -= 1
            self.saude -= 1
            self.idade += 1
    
    def pararDeComer(self):
        if self.comendo == True:
            print('Ele já não estava comendo! Não é possível parar de comer')
        else:
            print(f'O {self._nome} parou de comer.')
            self.comendo == False
            self._fome -= 1
            self.saude -= 1
            self.idade += 1

    def cuidarSaude(self):
        if self.saude >= 9:
            print(f'Não é necessário mais cuidar da saúde dele! Ele está com a saúde perfeita.')
        else:
            self.saude += 2
            print(f'Você cuidou da saúde do {self._nome}')