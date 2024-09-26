# 1- Crie uma classe chamada Veiculo com um método abstrato chamado ligar.
# 2- No mesmo arquivo, crie um construtor para a classe Veiculo que aceita os parâmetros marca e modelo.
# 3- Crie uma nova classe chamada Carro que herda da classe Veiculo.
# 4- No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e 
# atribua o atributo específico cor à classe filha.
# 5- Em um arquivo chamado main.py, importe a classe Carro.
# 6- No arquivo main.py, instancie três objetos da classe Carro com diferentes características, 
# como marca, modelo e cor.

from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo

    @abstractmethod
    def ligar(self):
        pass

    

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor

    def ligar(self):
        print(f"O carro {self.modelo} está ligado.")
    

carro1 = Carro('Fiat', 'Uno', 'Preto')
carro2 = Carro('Ford', 'Focus', 'Prata')
carro3 = Carro('Chevrolet', 'Voyage', 'Amarelo')

print(f'Carro1: Marca= {carro1._marca} | Modelo= {carro1._modelo} | Cor= {carro1.cor}')
print(f'Carro2: Marca= {carro2._marca} | Modelo= {carro2._modelo} | Cor= {carro2.cor}')
print(f'Carro3: Marca= {carro3._marca} | Modelo= {carro3._modelo} | Cor= {carro3.cor}')