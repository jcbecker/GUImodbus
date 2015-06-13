import serial
import time

class ModBusWriter:
	def __init__(self, outra):
		self.outra = outra
		
	def write(self, t):
		teste = serial.Serial(port = "/dev/pts/2", baudrate = 9600)
			
		try:
			teste.write(t + b'\n'.encode())				
		except:
			pass


objeto = ModBusWriter(None)
while True:
	m = raw_input("texto: ")
	objeto.write(m)

	
	
	
	
