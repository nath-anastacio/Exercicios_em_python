from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('Praça', 'Gourmet')
bebida_suco = Bebida('Suco de Laranja', 5.0, 'Grande')
bebida_suco.aplicar_desconto()
prato_franguinho = Prato('Frango Frito', 15.0, 'Frango empanado e frito.')
prato_franguinho.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_franguinho)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()