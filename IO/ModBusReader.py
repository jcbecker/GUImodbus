import time
from serial import Serial
from ModBusIO import ModBusIO
from ModBusWriter import ModBusWriter

class ModBusReader(ModBusIO):

	def __init__(self):
		self.function = "03"
		self.writer = ModBusWriter()

	def _checkSum(self, reg, regNumber):
		cs = int( self.slaveAddress, 16 ) + int( self.function, 16 ) 
		cs = cs + int( reg, 16 ) + int( regNumber, 16 )
		return hex( 255 - cs + 1 )[2:]

	def read(self, reg, regNumber ):
		
		confFile = open("GUImodbus/Conf/conf.txt","r")
		confFile.readline();
		rport = confFile.readline().split('[')[1].split(']')[0]
		
		sPort = Serial(port = rport, baudrate = 9600, timeout = 3)
		
		query = self.iniMSG + self.slaveAddress + self.function
		query = query + reg + regNumber + self._checkSum(reg,regNumber) + self.endMSG
		
		print query
		
		self.writer.write(query)
		
		word = ""
		while True:
			try:
				b = sPort.read()
				
				if b != '\n':
					if b is "":
						raise IOError("ReadTimeoutException")
						
					word += b
				else:
					return word						

			except Exception as e:
				raise e 
