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
	def write(self,reg,bit,data):
		msg = self.iniMSG + self.slaveAddress + self.function + reg + data + self._checkSum(reg[0:2], reg[2:], data[0:2], data[2:] )
		
		print msg.upper()
		serialPort.write(msg.upper())
		
