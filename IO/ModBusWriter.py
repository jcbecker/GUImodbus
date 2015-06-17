import time
from serial import Serial
from ModBusIO import *

class ModBusWriter(ModBusIO):
	
	def __init__(self):
		self.function = "06"

	def _checkSum(self, reg, regNumber):
		cs = int(self.slaveAddress, 16) + int(self.function, 16) 
		cs = cs + int(reg, 16) + int(regNumber, 16)
		return hex( 255 - cs + 1 )[2:]

	#so faz uma pergunta para o escravo
	#quem usa este metodo geralmente
	#e a classe de leitura.
	def question(self, t):
		
		try:
			serialPort.write(t)				
		except Exception as e:
			raise e

	#implementar
	def write(self,reg,bit,data):
		pass
