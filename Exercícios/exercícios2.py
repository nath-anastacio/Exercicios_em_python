##Exercício 1 

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = ['Rafael, Miguel, Daniel, Gabriel']
lista3 = [2002, 2024]

##Exercício 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

#for num in lista1:
    #print(num)

##Exercício 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

soma = 0
nova_lista = []
for num in lista1:
    if num%2!=0:
        soma = soma + num
        print(soma)

## Resolução do Exercício 3
soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)

##Exercício 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
lista1.sort(reverse = True)
for num in lista1:
    print(num)

## Resolução do Exercício 4
for i in range(10, 0, -1):
    print(i)
 
##Exercício 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
numero = int(input('Digite um numero: '))
print(f'A tabuada do número {numero} é:')
for num in lista1:
    print(num, 'x', numero,'= ',num*numero) 

## Resolução do Exercício 5
numero_tabuada = int(input("Digite um número para a tabuada: "))
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")

##Execício 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
lista4 = [10, 25, 15]
soma = 0
try:
    for num in lista4:
        soma = soma + num
        print(soma)
except:
    print('Falha ao somar os números da lista') 

## Resolução do Exercpicio 6
lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

##Exercício 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
def soma(num, num2, num3):
    resultado = num + num2 + num3
    return resultado

try:
    soma1 = soma(lista4[0], lista4[1], lista4[2])
    print('A soma dos valores é = ', soma1)
    print('A média dos valores é = ', soma1//len(lista4))
except:
    print('A lista está vazia!')

## Resolução do Exercício 7
lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")


