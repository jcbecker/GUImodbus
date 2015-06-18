import time
from serial import Serial
from ModBusIO import *

class ModBusWriter(ModBusIO):
	
	def __init__(self):
		self.function = "06"

	#so faz uma pergunta para o escravo
	#quem usa este metodo geralmente
	#e a classe de leitura.
	def question(self, t):
		
		try:
			serialPort.write(t)				
		except Exception as e:
			raise e

	#implementar
	def write(self,reg,data):
	
		msg = self.iniMSG + self.slaveAddress + self.function + reg + data
		
		msg = msg + self._checkSum(reg[0:2], reg[2:], data[0:2], data[2:] ) + self.endMSG
		
		msg = msg.upper()
		print "Escrita: " + msg
		serialPort.write(msg)

		#tem que ler a confirmacao =D
		word = ""
		while True:
			try:
				b = serialPort.read()
				
				if not "0d0a".decode('hex') in word:
					if b is "":
						raise IOError("ReadTimeoutException")
						
					word += b
				else:
					return word.upper() == msg					

			except Exception as e:
				raise e
