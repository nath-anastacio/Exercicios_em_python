###Exercícícios:
# 1- Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
# 2- Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
# 3- Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
# 4- Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
# 5- Altere o valor do atributo nome para 'Bistrô'.
# 6- Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
# 7- Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
# 8- Mude o estado da instância restaurante_pizza para ativo.
# 9- Imprima no console o nome e a categoria da instância restaurante_praca.

class restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praça = restaurante()
restaurante_praça.categoria = 'Italiana'
restaurante_praça.nome = 'Praça'

print(restaurante_praça.nome)
restaurante_ativo = 'O restaurante está ativo' if restaurante_praça.ativo else 'O restaurante está desativado'
print(restaurante_ativo)

#categoria = restaurante['categoria']
#print(categoria)

restaurante_praça.categoria ='Bistrô'
print(restaurante_praça.categoria)

restaurante_pizza = restaurante()
restaurante_pizza.nome = 'Pizza place'
restaurante_pizza.categoria = 'Fast Food'
print(f'a categoria do restaurante {restaurante_pizza.nome} é {restaurante_pizza.categoria}')
restaurante_pizza.ativo = True
print(restaurante_pizza.ativo)

print(f'nome: {restaurante_praça.nome} | categoria: {restaurante_praça.categoria}')

categoria2 = restaurante.categoria
print(categoria2)