import serial
import time

class ModBusReader:
			
	def read(self):
		
		confFile = open("../Conf/conf.txt","r")
		confFile.readline();
		rport = confFile.readline().split('[')[1].split(']')[0]
		
		sPort = serial.Serial(port = rport, baudrate = 9600, timeout = 1)
		
		word = ""
		while True:
			try:
				b = -1
				b = sPort.read()
				
				if b != '\n':
					if b is "":
						return
						
					word += b
				else:
					return word
		
			except:
				print("Reading error.")
				pass
				
	

objeto = ModBusReader()

while True:
	l = objeto.read()
	if l is not None:
		print(l)
	
	
	
