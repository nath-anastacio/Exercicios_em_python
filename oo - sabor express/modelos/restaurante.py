class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome
        self._categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def categoria(self):
        return self._categoria
    
    @property
    def ativo(self):
        return self._ativo

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')