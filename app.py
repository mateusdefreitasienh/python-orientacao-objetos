# Importa classe
from carro import Carro
from frota import Frota

# Cria o objeto frota

frota_IENH = Frota("IENH Transportes", "IENH", "93.425.750/0001-90")

# Instancia o objeto Carro
uno = Carro("Fiat", "Uno", 1994)
astra = Carro("GM", "Astra", 2007)
jetta = Carro("VW", "Jetta", 2010)

uno.acelerar()
uno.frear()
uno.set_placa("III-AAAA")

# Cadastra um carro na frota
frota_IENH.cadastra_carro(uno)
frota_IENH.cadastra_carro(astra)
frota_IENH.cadastra_carro(jetta)

frota_IENH.listar_frota()