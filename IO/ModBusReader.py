import serial
import time

class ModBusReader:
	def __init__(self, outra):
		self.outra = outra
		
			
	def read(self):
		sPort = serial.Serial(port = "/dev/pts/4", baudrate = 9600, timeout = 0.5)
		
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
				print("Exceção de leitura.")
				pass
				
	

objeto = ModBusReader(None)
while True:
	l = objeto.read()
	if l is not None:
		print(l)
	
	
	
