class BichinhoVirtual:
    def __init__(self, nome: str, fome: int, saude: int, idade: int):
        self._nome = nome
        self._fome = fome
        self.saude = saude
        self.idade = idade
        self.brincando = False
        self.comendo = False
    
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str):
            raise TypeError(f'O nome {valor} não é uma STRING!')
        valor = self._nome
    
    @property
    def fome(self):
        return self._fome
    @fome.setter
    def fome(self, valor):
        if not isinstance(valor, int):
            raise ValueError(f'O valor {valor} não é um INTEIRO!')
        return self._fome