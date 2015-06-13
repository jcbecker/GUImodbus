import serial
import time

class ModBusWriter:
		
	def write(self, t):
		confFile = open("../Conf/conf.txt","r")
		wport = confFile.readline().split('[')[1].split(']')[0]

		teste = serial.Serial(port = wport, baudrate = 9600)
			
		try:
			teste.write(t + b'\n'.encode())				
		except:
			pass


objeto = ModBusWriter()
while True:
	m = raw_input("texto: ")
	objeto.write(m)
