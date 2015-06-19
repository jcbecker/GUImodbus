from ..IO.ModBusReader import ModBusReader
from ..IO.ModBusWriter import ModBusWriter

class Lamp:

	comReg14 = {}
	comReg15 = {}
	comReg16 = {}

	def __init__(self):
		self.reader = ModBusReader()
		self.writer = ModBusWriter()

	def monitLamps(self):
		monitReg = "000B"
		regNumber = "0003"
		
		answer = self.reader.read(monitReg,regNumber)
		
		if answer[5:7] != "06":
			raise IOError ("Wrong answer exception")
		
		print answer
		lamps = []
		lamps.append( int( answer[7:11], 16 ) )
		lamps.append( int( answer[11:15], 16 ) )
		lamps.append( int( answer[15:19], 16 ) )
		
		#print int( answer[7:11], 16 )
		#print int( answer[11:15], 16 )
		#print int( answer[15:19], 16 )
		
		#lamps[0]: registrador 11
		#lamps[1]: registrador 12
		#lamps[3]: registrador 13
		
		return lamps


	def LampWrite(self, Reg, data):
		if not self.writer.write(Reg, data):
			if not self.writer.write(Reg, data):
				raise Exception("WriteException")
		else:
			return True

		
	def comLamp1(self,data):
		Reg = "000E"
		return self.LampWrite(Reg, data)

	def comLamp2(self,data):
		Reg = "000F"
		return self.LampWrite(Reg, data)

	def comLamp3(self,data):
		Reg = "0010"
		return self.LampWrite(Reg, data)
			
			
	
