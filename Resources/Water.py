# No fim esse comando para adcionar os modulos
# para reconhecimento do python, vai ser feito
# em apenas um arquivo.

from ..IO.ModBusReader import ModBusReader

class Water:

	test = 0	

	def __init__(self):	
		self.reg = {}	
		
	def testar(self):
		mr = ModBusReader()
		mr.read()
		print self.test

# preciso tirar duvidas sobre esse assunto 
# porque existem tres piscinas mas no registrador
# de numero 8 no bit 4 ele nao especifica.
