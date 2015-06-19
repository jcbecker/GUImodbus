from ..IO.ModBusReader import ModBusReader
from ..IO.ModBusWriter import ModBusWriter

class Lamp:

	monitReg11 = {}
	monitReg12 = {}
	monitReg13 = {}
	comReg14 = {}
	comReg15 = {}
	comReg16 = {}

	def __init__(self):
		self.reader = ModBusReader()

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
		
	def comLamp1(self,place):
		if self.comReg14.has_key(place):
			reg = self.comReg14[place]

			#pedir informacao
		else:
			return None

	def comLamp2(self,place):
		if self.comReg15.has_key(place):
			reg = self.comReg15[place]

			#pedir informacao
		else:
			return None

	def comLamp3(self,place):
		if self.comReg16.has_key(place):
			reg = self.comReg16[place]

			#pedir informacao
		else:
			return None
