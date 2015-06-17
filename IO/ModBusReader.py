import time
from serial import Serial
from ModBusIO import *
from ModBusWriter import ModBusWriter

class ModBusReader(ModBusIO):

	def __init__(self):
		
		self.function = "3033"
		self.writer = ModBusWriter()

	def _checkSum(self, reg, regNumber):
		cs = int( self.slaveAddress, 16 ) + int( self.function, 16 ) 
		cs = cs + int( reg, 16 ) + int( regNumber, 16 )
		return hex( 255 - cs + 1 )[2:]

	def read(self, reg, regNumber):
		
		###
		#confFile = open("GUImodbus/Conf/conf.txt","r")
		#confFile.readline();
		#rport = confFile.readline().split('[')[1].split(']')[0]
		#sPort = Serial(port = rport, baudrate = 9600, timeout = 3)
		###
		
		query = self.iniMSG + self.slaveAddress + self.function
		query = query + reg + regNumber + self._checkSum(reg,regNumber) + self.endMSG
		
		print query
		
		# Replace para poder escrever com espacos no meio
		self.writer.write(("3A 33 41 30 33 30 30 30 30 30 30 30 39 42 41 0D 0A").replace(" ", "").decode("hex"))
		print "sent: " +  ("3A 33 41 30 33 30 30 30 30 30 30 30 39 42 41 0D 0A").replace(" ", "").decode("hex")
		
		word = ""
		while True:
			try:
				b = serialPort.read()
				
				if not "0d0a".decode('hex') in word:
					if b is "":
						raise IOError("ReadTimeoutException")
						
					word += b
				else:
					print "received: " + word
					return word						

			except Exception as e:
				raise e 
