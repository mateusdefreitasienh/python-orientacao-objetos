class Carro:
    """
    Implementa o funcionamento de um carro
    """

    def __init__(self, marca: str, modelo: str, ano: int, placa = "ADS-2026"):
        """
        Construtor da classe Carro
        """
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.velocidade = 0

    def acelerar(self):
        """
        Acelera o carro em 10 km/h cada vez que é chamado
        """
        self.velocidade += 10
        self.get_velocidade()

    def frear(self):
        """
        Desacelera o carro em 10 km/h cada vez que é chamado
        """
        if self.velocidade > 0:
            self.velocidade -= 10
            self.get_velocidade()
        else:
            print("Carro já se encontra parado!")

    def get_velocidade(self):
        """
        Mostra a velocidade atual do carro
        """
        print(f"A velocidade atual do {self.modelo} é de {self.velocidade} km/h.")
        
    def get_placa(self):
        """
        Exibe a placa do carro
        """
        print(f"A placa do {self.modelo} é {self.placa}.")

    def set_placa(self, nova_placa):
        self.placa = nova_placa
        print(f"Placa atualizada para {self.placa}")