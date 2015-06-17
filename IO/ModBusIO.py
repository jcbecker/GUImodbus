from serial import Serial

serialPort = Serial(port = "/dev/pts/5", baudrate = 9600, timeout = 3)

#nao instancie essa classe.
class ModBusIO:
		
	iniMSG = ":"
	slaveAddress = "3341"
	endMSG = chr(13)+chr(10)	
