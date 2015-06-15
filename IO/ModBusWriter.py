import time
from serial import Serial
from ModBusIO import ModBusIO

class ModBusWriter(ModBusIO):
	
	def __init__(self):
		self.function = "06"

	def write(self, t):
		confFile = open("GUImodbus/Conf/conf.txt","r")
		wport = confFile.readline().split('[')[1].split(']')[0]

		msg = self.iniMSG + self.slaveAddress + self.function

		sComm = Serial(port = wport, baudrate = 9600)		
		
		try:
			sComm.write( t)				
		except Exception as e:
			raise e
			
	def _checkSum(self, reg, regNumber):
		cs = int( self.slaveAddress, 16 ) + int( self.function, 16 ) 
		cs = cs + int( reg, 16 ) + int( regNumber, 16 )
		return hex(cs)[2:]
