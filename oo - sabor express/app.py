from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Ana', 6)
restaurante_praca.receber_avaliacao('Gab', 8)

def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()