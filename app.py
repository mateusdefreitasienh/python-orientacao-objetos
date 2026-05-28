# Importa classe
from carro import Carros
from frota import Frotas
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

# frotas = GerenciadorFrotas("Localiza", "12.934-170/0001-70")
frotas = []

#Menu

def menu_frota(frota):
    msg += "C para cadastrar frota: \n"
    msg += "R para remover frota: \n"
    msg += "A para atualizar frota: \n"
    msg += "L para listar carros da frota: \n"
    msg += "V para voltar: \n"
    msg += "\nDigite a opção desejada: "

    opcao = input(msg).upper()
    
    if opcao == "C":
        nome = input("Digite o nome da Frota: ")
        empresa = input("Digite o nome da empresa: ")
        cnpj = input("Digite o CNPJ da empresa: ")
        nova_frota = Frotas(nome, empresa, cnpj)
        frotas.append(nova_frota)
        cadastro = input("Deseja cadastrar Frotas e carros? [S/N]: ")
        if cadastro.upper == "S":
            menu_frota(frotas[-1])
    elif opcao == "R":
        pass
    elif opcao == "A":
        pass
    elif opcao == "L":
        pass
    elif opcao == "L":
        pass
    elif opcao == "S":
        pass
    else:
        print("Comando inválido!")



def menu_principal():
    msg += "C para cadastrar frotas: \n"
    msg += "R para remover frotas: \n"
    msg += "A para atualizar frotas: \n"
    msg += "L para listar frotas: \n"
    msg += "S para sair: \n"
    msg += "\nDigite a opção desejada: "

    opcao = input(msg).upper()
    
    if opcao == "C":
        nome = input("Digite o nome da empresa: ")
        cnpj = input("Digite o CNPJ da empresa: ")
        nova_frota = GerenciadorFrotas(nome, cnpj)
        frotas.append(nova_frota)
        cadastro = input("Deseja cadastrar Frotas e carros? [S/N]: ")
        if cadastro.upper == "S":
            menu_frota(frotas[-1])
    elif opcao == "R":
        pass
    elif opcao == "A":
        pass
    elif opcao == "L":
        pass
    elif opcao == "L":
        pass
    elif opcao == "S":
        pass
    else:
        print("Comando inválido!")

opcao = ""

while True:
    menu_principal()