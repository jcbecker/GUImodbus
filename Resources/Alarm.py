from ..IO.ModBusWriter import ModBusWriter
from ..IO.ModBusReader import ModBusReader

class Alarm:

	monitRegBits = {}

	def __init__(self):		
		self.writer = ModBusWriter()
		self.reader = ModBusReader()
		
		self.monitRegBits['garagem']     = 0
		self.monitRegBits['piscina1']    = 1
		self.monitRegBits['cozinha']     = 2
		self.monitRegBits['saladeestar'] = 3
		self.monitRegBits['saladejogos'] = 4
		self.monitRegBits['suite'] 	  	 = 5
		self.monitRegBits['dormitorio1'] = 6
		self.monitRegBits['dormitorio2'] = 7
		
	def ONOFF( self ):
		comReg = "0008"
	
		#usar o bit 0 do registrador 8 para
		#ligar ou desligar o alarme da casa.
		
	def checkONOFF( self ):
		monitReg = "0001"
		regNumber = "0001"
		
		print "resposta: " + self.reader.read(monitReg,regNumber)	
		
		#usar o bit 0 do registrador 9 para 
		#verificar se o alarme esta ligado ou desligado.
	
	#usa o bit 1 do registrador 9 para
	#verificar se o alarme esta disparado
	#se o mesmo esta disparado retorna true
	#senao false
	def fired( self ):	
		monitReg = "0009"
		regNumber = "0001"
		
		answer = self.reader.read(monitReg, regNumber)

		bc = answer[5]+answer[6]

		if bc != "02":
			print "Resposta errada: "+ answer
			#raise IOError("WrongAnswerException")

		return ( int( answer[7:11], 16 ) & 2 ) != 0

	def checkAlarm(self, place ):
		
		if self.monitRegBits.has_key( place ):
			monitReg = "000A"
			regNumber = "0001"

			#montar mensagem e verificar
			#o status do alarm de um lugar em especifico
		else: 
			return None
 
		
