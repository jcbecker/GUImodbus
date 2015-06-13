import serial
import time

class ModBusIO:
	def __init__(self, outra):
		self.outra = outra
		
	def write(self, t):
		teste = serial.Serial(port = "/dev/pts/3", baudrate = 9600)
			
		try:
			teste.write(t + b'\n'.encode())				
		except:
			pass


objeto = ModBusIO(None)
while True:
	m = raw_input("texto: ")
	objeto.write(m)

	
	
	
	
