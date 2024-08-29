#Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. 
# Inicie o atributo ativo como False por padrão.
#Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta.
#Crie duas instâncias da classe e imprima essas instâncias.
#Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. 
#Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
#Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.
#Crie uma instância da classe e imprima o valor da propriedade titular.
#Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. 
#Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
#Crie um método de classe para a conta ClienteBanco.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False
    def __str__(self):
        return f'Titular = {self.titular} | Saldo = R${self.saldo} | {self.ativo}'
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True
    @property
    def ativo(self):
        if self._ativo:
            return 'A conta bancária está ativada!'
        else:
            return 'A conta está desativada'
        
conta1 = ContaBancaria('Maria', 5200)
print(conta1)
print(conta1._ativo)
conta1.ativar_conta
print(conta1)    

class ClienteBanco:
    def __init__(self, nome, idade, email, telefone, cpf):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
        self.saldo = cpf
    def __str__(self):
        return f'Nome = {self.nome} |Idade = {self.idade} |e-mail = {self.email} |tel.: {self.telefone} |Saldo = R${self.saldo}'
    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancariaPythonica(titular, saldo_inicial)
        return conta
    
class ContaBancariaPythonica:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular
    @property
    def saldo(self):
        return self._saldo
    @property
    def ativo(self):
        return self._ativo

cliente1 = ClienteBanco('Joana', 32, 'joana@gmail.com', 99999999, 4078)
cliente2 = ClienteBanco('Amelie', 57, 'amelie123@hotmail.com', 88888888, 17000)
cliente3 = ClienteBanco('Renato', 64, 'renatosoares1@gmail.com', 777777777, 3670)
conta4 = ContaBancariaPythonica('Luara', 3450)

cliente1_conta = ClienteBanco.criar_conta('Joana', 4078)

print(cliente1)
print()
print(f'Conta de {cliente1_conta.titular} criada com sucesso com o saldo inicial de R${cliente1_conta.saldo}.')
print()
print(cliente2)
print()
print(cliente3)   
print()
print(f'Titular da conta4: {conta4.titular} | Saldo = R${conta4.saldo}')
print('########### FIM ############')

