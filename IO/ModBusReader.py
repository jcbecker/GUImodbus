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
						raise NameError("ReadTimeoutException")
						
					word += b
				else:
					return word
		
			except Exception as e:
				if e == "ReadTimeoutException":
					
					print e
				#else:
				#	print "Other read exception."
						
	

objeto = ModBusReader()

while True:
	try:
		l = objeto.read()
	except("ReadTimeoutException"):
		print "jhLAJLIHLlllllllll"
	if l is not None:
		print(l)
	
	
	
