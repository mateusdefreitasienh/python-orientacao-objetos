class GerenciadorFrotas:
    """
    Classe que gerencia as frotas.
    """
    def __init__(self, nome: str, cnpj: str):
        """
        Construtor da classe Gerenciador de frotas
        """
        self.nome = nome
        self.cnpj = cnpj
        self.frotas = []

    def cadastra_frota(self, frota):
        """
        Cadastra uma nova frota
        """
        self.frotas.append(frota)
        print("Frota cadastrada com sucesso!")

    def listar(self):
        """
        Lista todas as frotas
        """
        print(10*"=" + " Lista de frotas cadastradas " + 10*"=")
        for frota in self.frotas:
            print(frota)
        print(50*"=")