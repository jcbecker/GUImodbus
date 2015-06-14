# No fim esse comando para adcionar os modulos
# para reconhecimento do python, vai ser feito
# em apenas um arquivo.

from ..IO.ModBusReader import ModBusReader

class Water:
	
	def __init__(self):	
		self.reg = {}	

	test = 3
		
	def testar(self):
		mr = ModBusReader()
		print(self.test)
w = Water()
w.testar()
# preciso tirar duvidas sobre esse assunto 
# porque existem tres piscinas mas no registrador
# de numero 8 no bit 4 ele nao especifica.
