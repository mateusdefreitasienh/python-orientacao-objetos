# Importa classe
from carro import Carro
from frota import Frota
from gerenciador import GerenciadorFrotas

# # Cria o objeto frota

# frota_IENH = Frota("IENH Transportes", "IENH", "93.425.750/0001-90")

# # Instancia o objeto Carro
# uno = Carro("Fiat", "Uno", 1994)
# astra = Carro("GM", "Astra", 2007)
# jetta = Carro("VW", "Jetta", 2010)

# uno.acelerar()
# uno.frear()
# uno.set_placa("III-AAAA")

# # Cadastra um carro na frota
# frota_IENH.cadastra_carro(uno)
# frota_IENH.cadastra_carro(astra)
# frota_IENH.cadastra_carro(jetta)

# frota_IENH.listar_frota()

gerenciador = GerenciadorFrotas("Localiza", "12.934-170/0001-70")
# frotas = []

#Menu

def menu_carro(posicao):
    msg = "========== CADASTRO DE CARRO ==========\n"
    msg += "C para cadastrar carro: \n"
    msg += "R para remover carro: \n"
    msg += "A para atualizar carro: \n"
    msg += "L para listar carros: \n"
    msg += "V para voltar: \n"
    msg += "\nDigite a opção desejada: "

    opcao = input(msg).upper()
    
    if opcao == "C":
        marca = input("Digite a marca do carro: ")
        modelo = input("Digite o modelo do carro: ")
        ano = input("Digite o ano do carro: ")
        placa = input("Digite a placa do carro: ")
        novo_carro = Carro(marca, modelo, ano, placa)
        gerenciador.frotas[posicao].cadastrar_carro(novo_carro)
        cadastro = input("Deseja cadastrar carros? [S/N]: ")
        if cadastro.upper == "S":
            menu_carro(-1)
    elif opcao == "R":
        pass
    elif opcao == "A":
        pass
    elif opcao == "L":
        gerenciador.frotas[posicao].listar()
    elif opcao == "L":
        pass
    elif opcao == "V":
        menu_frota()
    else:
        print("Comando inválido!")



def menu_frota():
    msg = "========== CADASTRO DE FROTA ==========\n"
    msg += "C para cadastrar frota: \n"
    msg += "R para remover frota: \n"
    msg += "A para atualizar frota: \n"
    msg += "L para listar carros da frota: \n"
    msg += "S para sair: \n"
    msg += "\nDigite a opção desejada: "

    opcao = input(msg).upper()
    
    if opcao == "C":
        nome = input("Digite o nome da Frota: ")
        empresa = input("Digite o nome da empresa: ")
        cnpj = input("Digite o CNPJ da empresa: ")
        nova_frota = Frota(nome, empresa, cnpj)
        gerenciador.cadastra_frota(nova_frota)
        cadastro = input("Deseja cadastrar carros? [S/N]: ")
        if cadastro.upper() == "S":
            menu_carro(-1)
    elif opcao == "R":
        pass
    elif opcao == "A":
        pass
    elif opcao == "L":
        gerenciador.listar()
    elif opcao == "S":
        return
    else:
        print("Comando inválido!")

opcao = ""

while True:
    menu_frota()
    break