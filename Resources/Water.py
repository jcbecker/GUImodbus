# No fim esse comando para adcionar os modulos
# para reconhecimento do python, vai ser feito
# em apenas um arquivo.
import sys
sys.path.append('../IO/')

from ModBusReader import ModBusReader

class Water:
	
	def __init__(self):	
		self.reg = {}	

# preciso tirar duvidas sobre esse assunto 
# porque existem tres piscinas mas no registrador
# de numero 8 no bit 4 ele nao especifica.