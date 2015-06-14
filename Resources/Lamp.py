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
		monitReg11['saladeestar1'] = 0
		monitReg11['saladeestar2'] = 1
		monitReg11['saladeestar3'] = 2
		monitReg11['saladejantar1'] = 3
		monitReg11['saladejantar2'] = 4
		monitReg11['saladejogos1'] = 5
		monitReg11['saladejogos2'] = 6
		monitReg11['dormitorio1'] = 7

		monitReg12['bwc1'] = 0
		monitReg12['circulacao'] = 1
		monitReg12['dormitorio2'] = 2
		monitReg12['closed'] = 3
		monitReg12['bwc2'] = 4
		monitReg12['suite1'] = 5
		monitReg12['suite2'] = 6
		monitReg12['suite3'] = 7
		
		monitReg13['bwc'] = 0
		monitReg13['deposito'] = 1
		monitReg13['varandadapiscina'] = 2
		monitReg13['piscina1'] = 3
		monitReg13['piscina2'] = 4
		monitReg13['piscina3'] = 5

		comReg14['saladeestar1'] = 0
		comReg14['saladeestar1'] = 1
		comReg14['saladeestar1'] = 2
		comReg14['saladeestar1'] = 3
		comReg14['saladeestar1'] = 4
		comReg14['saladeestar1'] = 5
		comReg14['saladeestar1'] = 6
		comReg14['saladeestar1'] = 7
		
		comReg15['bwc1'] = 0
		comReg15['circulacao'] = 1
		comReg15['dormitorio2'] = 2
		comReg15['closed'] = 3
		comReg15['bwc2'] = 4
		comReg15['suite1'] = 5
		comReg15['suite2'] = 6
		comReg15['suite3'] = 7

		comReg16['bwc'] = 0
		comReg16['deposito'] = 1
		comReg16['varandadapiscina'] = 2
		comReg16['piscina1'] = 3
		comReg16['piscina2'] = 4
		comReg16['piscina3'] = 5

	def monitLamps1(self,place):
		if monitReg11.has_key(place):
			reg = monitReg11[place]

			#pedir informacao
		else:
			return None

	def monitLamps2(self,place):
		if monitReg12.has_key(place):
			reg = monitReg12[place]

			#pedir informacao
		else:
			return None

	def monitLamps3(self,place):
		if monitReg13.has_key(place):
			reg = monitReg13[place]

			#pedir informacao
		else:
			return None

	def comLamp1(self,place):
		if comReg14.has_key(place):
			reg = comReg14[place]

			#pedir informacao
		else:
			return None

	def comLamp2(self,place):
		if comReg15.has_key(place):
			reg = comReg15[place]

			#pedir informacao
		else:
			return None

	def comLamp3(self,place):
		if comReg16.has_key(place):
			reg = comReg16[place]

			#pedir informacao
		else:
			return None
