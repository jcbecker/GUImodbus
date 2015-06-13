import serial
import time

class ModBusIO:
	def __init__(self, outra):
		self.outra = outra
		
		
	# Funcao para ler da porta serial. Le ate achar um \n e retorna 
	# a string concatenada caractere a caractere.	
	def read(self):
		sPort = serial.Serial(port = "/dev/pts/3", baudrate = 9600 )
		
		word = ""
		while True:
			try:
				sPort.timeout = 6
				b = sPort.read()
				
				
				
				if b != '\n':
					word += b
				else:
					return word
		
			except:
				print("Deu um exception")
				pass

objeto = ModBusIO(None)
while True:
	print(objeto.read())
	print("teste:")
	
	
	
