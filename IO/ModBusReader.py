import time
from serial import Serial
from ModBusIO import *
from ModBusWriter import ModBusWriter

class ModBusReader(ModBusIO):

	def __init__(self):		
		self.function = "03"
		self.writer = ModBusWriter()
		
	#receber numero do registrador e numero de registradores em hexa.
	def read(self, reg, regNumber):
		
		query = self.iniMSG + self.slaveAddress + self.function
		query = query + reg + regNumber + self._checkSum(reg[0:2], reg[2:],regNumber[0:2],regNumber[2:]) + self.endMSG
		
		self.writer.question( query.upper() )
		
		#para debug.		
		#print "sent: " +  ("3A 33 41 30 33 30 30 30 39 30 30 30 31 42 39 0D 0A").replace(" ", "").decode("hex")
		
		word = ""
		while True:
			try:
				b = serialPort.read()
				
				if not "0d0a".decode('hex') in word:
					if b is "":
						raise IOError("ReadTimeoutException")
						
					word += b
				else:
					return word.upper()					

			except Exception as e:
				raise e 
