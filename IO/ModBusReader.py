import time
from serial import Serial

class ModBusReader:
			
	def read(self):
		
		confFile = open("../Conf/conf.txt","r")
		confFile.readline();
		rport = confFile.readline().split('[')[1].split(']')[0]
		
		sPort = serial.Serial(port = rport, baudrate = 9600, timeout = 1)
		
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
