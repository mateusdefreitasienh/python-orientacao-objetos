class Frota:
    """
    Implementa o gerenciamento de uma frota de carros
    """
    def __init__(self, nome, empresa, cnpj):
        """
        Construtor da classe
        """
        self.nome = nome
        self.empresa = empresa
        self.cnpj = cnpj
        self.carros = [] # lista de carros

    def cadastra_carro(self, carro):
        """
        Cadastra carros na frota
        """
        self.carros.append(carro) #adiciona o carro na lista
    
    def listar_frota(self):
        """
        Imprime todos os carros da frota
        """
        print(f"A frota {self.nome} tem os seguintes carros: ")

        for carro in self.carros:
            print(carro)