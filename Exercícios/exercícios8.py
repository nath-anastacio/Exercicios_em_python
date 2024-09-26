#Criando uma classe pai(Banco) e uma classe filho(Agência):

class Banco:
    def __init__(self, nome, endereco):
        self._nome = nome
        self._endereco = endereco
    
class Agencia(Banco):
    def __init__(self, nome, endereco, numero):
        super().__init__(nome, endereco)
        self._numero = numero

################################################################
#Criando a classe pai(Veiculo) e as classes filho(Carro e Moto)

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    def __str__(self):
        status = 'ligado' if self._ligado else 'desligado'
        return f'O veiculo da marca {self.marca} e modelo {self.modelo} está {status}'

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas
    
    def __str__(self):
        status = 'ligado' if self._ligado else 'desligado'
        return f'{self.marca}, {self.modelo}, {self.portas} - {status}'
    
class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo
    
    def __str__(self):
        status = 'ligado' if self._ligado else 'desligado'
        return f'{self.marca}, {self.modelo}, {self.tipo} - {status}'

###################################################################
#Instanciando as classes

moto1 = Moto('Kawazaki', 1.0, 'casual')
moto2 = Moto('Honda', 2.4, 'esportiva')
carro1 = Carro('Chevrolet', 'Celta', 2)
carro2 = Carro('Volksvagen', 'Voyage', 3)

print(carro1)
print(carro2)
print(moto1)
print(moto2)