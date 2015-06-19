from ..IO.ModBusReader import ModBusReader

class Temperature:
	reg = {}
	
	def __init__(self):
		self.reader = ModBusReader()

		# numero do registrador de cada local
		# cada local ocupa um registrador 
		# inteiro.
		self.reg['piscina']  	= 0
		self.reg['banheira'] 	= 1
		self.reg['suite'] 	= 2
		self.reg['saladeestar'] = 3
		self.reg['saladejogos'] = 4
		self.reg['dormitorio1'] = 5
		self.reg['dormitorio2'] = 6

	#le a temperatura de todos os lugares que possuem sensor.
	def readTemp(self):
		monitReg = "0000"
		regNumber = "0007"

		answer = self.reader.read(monitReg,regNumber)

		if answer[5]+answer[6] != "0E":
			raise IOError("WrongAnswerException")

		ini = 7
		end = 11
		temperatures = []
		for _ in range(7):
			temperatures.append( answer[ini:end] )
			ini = end
			end = end + 4

		return temperatures

	#se precisar fazer uma funcao para pegar
	#a temperatura de um local especifico.
	def check(self, place ):
		if self.reg.has_key(place):
			checkReg = self.reg[place]

			# montar a mensagem no protocolo ModBus
			# e utilizar o ModBusReader para ler a temperatura.
			# e entao retornar a mesma.
			print(checkReg)
		else:
			return None
