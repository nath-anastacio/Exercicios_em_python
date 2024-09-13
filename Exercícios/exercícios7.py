#Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao.
#Inicie um atributo chamado disponivel como True por padrão.
#Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor 
#e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.
#Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False.
#Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.
#Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro
#e retorna uma lista dos livros disponíveis publicados nesse ano.


class Livro:
    biblioteca = []

    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        Livro.biblioteca.append(self)

    def __str__(self):
        return f"Livro: {self.titulo} | Autor: {self.autor} | Ano de Publicação: {self.ano_publicacao}"

    def emprestar(self):
        self.disponivel = False
        
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.biblioteca if livro.ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis
    
livro1 = Livro("Python Cookbook", "Samuel Developer", 2019)
print(f"Antes de emprestar: Livro disponível? {livro1.disponivel}")
livro1.emprestar()
print(f"Depois de emprestar: Livro disponível? {livro1.disponivel}")

print(livro1)

livro2 = Livro("Python in Practice", "Emily Coder", 2021)
print(f"Antes de emprestar: Livro disponível? {livro2.disponivel}")
livro2.emprestar()
print(f"Depois de emprestar: Livro disponível? {livro2.disponivel}")

print(livro2)