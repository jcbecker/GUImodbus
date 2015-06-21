from serial import Serial
import threading

lock = threading.RLock()
lock.acquire()
serialPort = Serial(port = "/dev/pts/17", baudrate = 9600, timeout = 1)
lock.release()

#nao instancie essa classe.
class ModBusIO:
		
	iniMSG = ":"
	slaveAddress = "3A"
	endMSG = chr(13)+chr(10)
	
	def _checkSum(self, reg1, reg2, value1, value2 ):
		cs = int(self.slaveAddress, 16) + int(self.function, 16) 
		cs = cs + int(reg1, 16) + int(reg2, 16) + int(value1, 16) + int(value2, 16)
		
		if cs > 255 :
			cs = int( bin(255 - cs + 1)[3:], 2 )
			
		return hex( 255 - cs + 1 )[2:]	
