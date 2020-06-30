class Bola:
    def __init__(self, cor, circuferencia, material):
        self.cor = cor
        self.circuferencia = circuferencia
        self.material = material

    # Getter
    @property
    def circuferencia(self):
        return self._circuferencia

    # Setter
    @circuferencia.setter
    def circuferencia(self, valor):
        self._circuferencia = valor
        if isinstance(valor, str):
            self.circuferencia = float(valor.replace('cm', ''))
