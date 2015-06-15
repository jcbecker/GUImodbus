from Resources.Water import Water
from IO.ModBusWriter import ModBusWriter

writer = ModBusWriter()

while True:
	ask = raw_input("Digite uma string: ")
	writer.write(ask)
