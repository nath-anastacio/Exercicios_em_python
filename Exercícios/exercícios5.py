# 1- Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
# 2- Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
# 3- Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
# 4- Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
# 5- Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

class Carro:
    carros = []
    def __init__(self, marca, cor, preco):
        self.marca = marca
        self.cor = cor
        self.preco = preco

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo}'
    
carro1 = Carro('Volksvagen', 'Amarelo', 50.000)
restaurante1 = Restaurante('Praça', 'Comida italiana')

restaurante2 = Restaurante('Sushi master', 'Comida japonesa')

print(restaurante1)


class Cliente:
    def __init__(self, nome, idade, genero, telefone):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.telefone = telefone
    def __str__(self):
        return f'{self.nome} | {self.idade} | {self.genero} | {self.telefone}'
    

cliente1 = Cliente('Carla', 46, 'Feminino', 21973172937)
cliente2 = Cliente('Maymontilla', 56, 'Feminino', 000000000)
cliente3 = Cliente('Adriano', 48, 'Masculino', 0000000000)


print(cliente1)       
print(cliente2)
print(cliente3)

########################################################
#Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. 
# Adicione um método especial __str__ para imprimir uma representação em string da pessoa. 
# Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. 
# Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada 
# com base na profissão da pessoa.

class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    
    def __str__(self):
        return f'Nome = {self.nome} | Idade = {self.idade} | Profissão = {self.profissao}'
    
    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá! Meu nome é {self.nome} e eu trabalho como {self.profissao}!'
        else:
            return f'Olá meu nome é {self.nome}!'
    
    def aniversario(self):
        self.idade +=1

pessoa1 = Pessoa('Maria', 45, 'cabeleireira')
print(pessoa1.saudacao())
print(pessoa1)