# No fim esse comando para adcionar os modulos
# para reconhecimento do python, vai ser feito
# em apenas um arquivo.

from ..IO.ModBusReader import ModBusReader

class Temperature:
	reg = {}
	
	def __init__(self):
		# numero do registrador de cada local
		# cada local ocupa um registrador 
		# inteiro.
		self.reg['piscina']  	= 0
		self.reg['banheira'] 	= 1
		self.reg['suite'] 		= 2
		self.reg['saladeestar'] = 3
		self.reg['saladejogos'] = 4
		self.reg['dormitorio1'] = 5
		self.reg['dormitorio2'] = 6

	def check(self, place ):
		if self.reg.has_key(place):
			checkReg = self.reg[place]

			# montar a mensagem no protocolo ModBus
			# e utilizar o ModBusReader para ler a temperatura.
			# e entao retornar a mesma.
			print(checkReg)
		else:
			return None
