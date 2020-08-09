from classes.bichinho import BichinhoVirtual

class bichinho(BichinhoVirtual):
    def __init__(self, nome, fome, saude, idade):
        super().__init__(nome, fome, saude, idade)
    
    def statusFome(self):
        if self._fome <= 1:
            print(f'O {self._nome} está morrendo de fome! Ajude-o o alimentando!')
        elif self._fome <= 4:
            print(f'O {self._nome} está com fome!')
        elif self._fome <= 5:
            print(f'O {self._nome} não está com fome!')
        elif self._fome <= 9:
            print(f'O {self._nome} está sem fome!')
        else:
            print(f'O {self._nome} está totalmente satisfeito de comida!')
    
    def statusSaude(self):
        if self.saude <= 1:
            print(f'O {self._nome} esta morrendo, ajude-o a se curar!!!')
        elif self.saude <= 4:
            print(f'O {self._nome} esta com a saúde baixa, talvez seja um bom momento para um remédio.')
        elif self.saude <= 5:
            print(f'O {self._nome} esta com a saúde boa!')
        elif self.saude <= 9:
            print(f'O {self._nome} esta bem de saúde!')
        else:
            print(f'O {self._nome} esta com a saúde perfeita!')

    def statusHumor(self):
        if (self._fome + self.saude) / 2  <= 1:
            print(f'O {self._nome} está muito mau humorado!')
        elif (self._fome + self.saude) / 2  <= 4:
            print(f'O {self._nome} não está bem humorado')
        elif (self._fome + self.saude) / 2  <= 5:
            print(f'O {self._nome} não está bem humorado')
        elif (self._fome + self.saude) / 2  <= 9:
            print(f'O {self._nome} está bem humorado!')
        else:
            print(f'O {self._nome} está totalmente humorado!!')

    def statusIdade(self):
        if self.idade < 2:
            print(f'O {self._nome} tem {self.idade} ano! Ele é um bebê ainda!')
        elif self.idade < 5:
            print(f'O {self._nome} tem {self.idade} anos! Ele já é uma criança')
        elif self.idade < 7:
            print(f'O {self._nome} tem {self.idade} anos! Ele já é um adolescente')
        elif self.idade < 9:
            print(f'O {self._nome} tem {self.idade} anos! Ele já é um adulto')
        else:
            print(f'O {self._nome} tem {self.idade} anos! Ele já é um idoso!')
        

    def status(self):
        if (self.comendo == False) and (self.brincando == False):
            if (self.fome > 1) and (self.saude > 1):
                self.statusHumor()
                self.statusFome()
                self.statusSaude()
                self.statusIdade()
                print(f'O {self._nome} não está comendo nem brincando!')
                self._fome -= 1
                self.saude -= 1
                self.idade += 1
            elif (self.fome <= 1) or (self.saude <= 1):
                print(f'O {self._nome} está muito cansado! Não é possível ver o status dele agora! Que tal alimentar ele e cuidar da saúde dele?')
        else:
            if self.comendo == True:
                self.statusHumor()
                self.statusFome()
                self.statusSaude()
                self.statusIdade()
                self._fome -= 1
                self.saude -= 1
                self.idade += 1
                print(f'O {self._nome} está comendo')
            elif self.brincando == True:
                self.statusHumor()
                self.statusFome()
                self.statusSaude()
                self.statusIdade()
                self._fome -= 1
                self.saude -= 1
                self.idade += 1
                print(f'O {self._nome} está brincando')


