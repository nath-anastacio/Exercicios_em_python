from modelos.avaliacoes import Avaliacao

class Restaurante:
    """Representa um restaurante e suas características"""
    restaurantes = []

    def __init__(self, nome, categoria):
        """Inicializa uma instância de restaurantes.
    
    Parâmetros:
    - nome (str): O nome do restaurante.
    - categoria (str): A categoria do restaurante."""
        self._nome = nome
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    
    @property
    def nome(self):
        """Retorna uma representação em string do restaurante."""
        return self._nome
    
    @property
    def categoria(self):
        return self._categoria
    
    @property
    def ativo(self):
        return self._ativo

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista de todos os restaurantes."""
        for restaurante in Restaurante.restaurantes:
            print(f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(20)} | {'Status'}')
            print(f'{restaurante.nome.ljust(22)} | {restaurante.categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante.ativo}')

    def ativo(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""
        return '⌧' if self._ativo else '☐'

    def receber_avaliacao(self, cliente, nota):
        """Registra uma avaliação para o restaurante.
        
        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (int): Nota atribuída ao restaurante. """
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        """Calcula e retorna a média das avaliações do restaurante."""
        if not self._avaliacao:
            return '--'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

