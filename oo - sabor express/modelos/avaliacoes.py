class Avaliacao:
    def __init__(self, cliente, nota):
        """Inicializa uma instância de uma avaliação.
        
        Parâmetros:
        - cliente (str): Nome do cliente que fez a avaliação.
        - nota (int): Nota atribuída ao restaurante."""
        self._cliente = cliente
        self._nota = nota

    @property
    def cliente(self):
        return self._cliente
    
    @property
    def nota(self):
        return self._nota

    def __str__(self):
        return f'Cliente: {self.cliente} | Nota: {self.nota}'