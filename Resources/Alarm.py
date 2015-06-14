# No fim esse comando para adcionar os modulos
# para reconhecimento do python, vai ser feito
# em apenas um arquivo.

from ..IO.ModBusWriter import ModBusWriter
from ..IO.ModBusReader import ModBusReader

class Alarm:

	monitRegBits = {}

	def __init__(self):		
		self.monitRegBits['garagem']     = 0
		self.monitRegBits['piscina']     = 1
		self.monitRegBits['cozinha']     = 2
		self.monitRegBits['saladeestar'] = 3
		self.monitRegBits['saladejogos'] = 4
		self.monitRegBits['suite'] 		 = 5
		self.monitRegBits['dormitorio1'] = 6
		self.monitRegBits['dormitorio2'] = 7

	def checkAlarm(self, place ):
		
		#ainda precisa tratar o
		#parametro place.
		if self.has_key( place ):
			monitReg = 10		
			bitCheck = self.mintRegBits[place]

			#montar mensagem e verificar
			#o status do alarm
		else: 
			return None

	def fired( self ):	
		monitReg = 9

		#usar o bit 1 do registrador 9 para
		#verificar se o alarme esta disparado.	

	def checkONOFF( self ):
		monitReg = 9
		
		#usar o bit 0 do registrador 9 para 
		#verificar se o alarme esta ligado ou desligado.

	def ONOFF( self ):
		comReg = 8
	
		#usar o bit 9 do registrador 8 para
		#ligar ou desligar o alarme da casa. 
		
