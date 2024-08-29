##Exercício 1

pessoa = {'nome' : 'Nathalia', 'idade' : 21, 'cidade' : 'Belford Roxo'}
print(pessoa)

##Exercício 2 - 
"""Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
Adicione um campo de profissão para essa pessoa;
Remova um item do dicionário."""

pessoa['idade'] = 22
print(pessoa)
pessoa['profissão'] = 'Analista'
print(pessoa)
del pessoa['profissão']
print(pessoa)

##Exercício 3 -  Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.
numeros_e_seus_quadrados = {'1 =':1**2 , '2 =' : 2**2, '3 =' : 3**2, '4 =' : 4**2, '5 =' : 5**2}
print(numeros_e_seus_quadrados)

##Resolução exercício 3
numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)

##Exercício 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
pessoas = {'maria':{'nome': 'Maria', 'idade' : 45, 'cidade' : 'Belford Roxo', 'profissão': 'Cabelereira'},
           'nathalia':{'nome': 'Nathalia Anastacio', 'idade': 21, 'cidade': 'Belford Roxo', 'profissao': 'nenhuma'}
           }
if 'nome' in pessoas:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")

print(pessoas['maria']['idade'])

##Exercício 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
## Resolução:
frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)
