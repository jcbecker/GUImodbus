import time
from serial import Serial

class ModBusWriter:
		
	def write(self, t):
		confFile = open("GUImodbus/Conf/conf.txt","r")
		wport = confFile.readline().split('[')[1].split(']')[0]

		teste = Serial(port = wport, baudrate = 9600)
			
		try:
			teste.write(t + b'\n'.encode())				
		except Exception as e:
			raise e
