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
		self.monitReg11['saladeestar1'] = 0
		self.monitReg11['saladeestar2'] = 1
		self.monitReg11['saladeestar3'] = 2
		self.monitReg11['saladejantar1'] = 3
		self.monitReg11['saladejantar2'] = 4
		self.monitReg11['saladejogos1'] = 5
		self.monitReg11['saladejogos2'] = 6
		self.monitReg11['dormitorio1'] = 7

		self.monitReg12['bwc1'] = 0
		self.monitReg12['circulacao'] = 1
		self.monitReg12['dormitorio2'] = 2
		self.monitReg12['closed'] = 3
		self.monitReg12['bwc2'] = 4
		self.monitReg12['suite1'] = 5
		self.monitReg12['suite2'] = 6
		self.monitReg12['suite3'] = 7
		
		self.monitReg13['bwc'] = 0
		self.monitReg13['deposito'] = 1
		self.monitReg13['varandadapiscina'] = 2
		self.monitReg13['piscina1'] = 3
		self.monitReg13['piscina2'] = 4
		self.monitReg13['piscina3'] = 5

		self.comReg14['saladeestar1'] = 0
		self.comReg14['saladeestar1'] = 1
		self.comReg14['saladeestar1'] = 2
		self.comReg14['saladeestar1'] = 3
		self.comReg14['saladeestar1'] = 4
		self.comReg14['saladeestar1'] = 5
		self.comReg14['saladeestar1'] = 6
		self.comReg14['saladeestar1'] = 7
		
		self.comReg15['bwc1'] = 0
		self.comReg15['circulacao'] = 1
		self.comReg15['dormitorio2'] = 2
		self.comReg15['closed'] = 3
		self.comReg15['bwc2'] = 4
		self.comReg15['suite1'] = 5
		self.comReg15['suite2'] = 6
		self.comReg15['suite3'] = 7

		self.comReg16['bwc'] = 0
		self.comReg16['deposito'] = 1
		self.comReg16['varandadapiscina'] = 2
		self.comReg16['piscina1'] = 3
		self.comReg16['piscina2'] = 4
		self.comReg16['piscina3'] = 5

	def monitLamps1(self,place):
		if self.monitReg11.has_key(place):
			reg = self.monitReg11[place]

			#pedir informacao
		else:
			return None

	def monitLamps2(self,place):
		if self.monitReg12.has_key(place):
			reg = self.monitReg12[place]

			#pedir informacao
		else:
			return None

	def monitLamps3(self,place):
		if self.monitReg13.has_key(place):
			reg = self.monitReg13[place]

			#pedir informacao
		else:
			return None

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
