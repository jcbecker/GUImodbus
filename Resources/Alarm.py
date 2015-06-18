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
		
	#usa o bit 0 do registrador 8 para
	#ligar ou desligar o alarme da casa
	#retorna false se o alarme foi desligado
	#retorna true se o alarme foi ligado.
	def ONOFF( self ):
		comReg = "0008"
		regNumber = "0001"

		answer = self.reader.read( comReg, regNumber )

		if answer[5]+answer[6] != "02":
			raise IOError("AlarmAnswerException")	

		regData = int( answer[7:11], 16 )

		if regData & 1:
			regData = regData - 1
			self.state = False
		else:
			self.state = True
			regData = regData + 1

		regData = hex(regData)[2:]

		l = len(regData)

		if l == 1:
			regData = "000"+regData
		elif l == 2:
			regData = "00"+regData
		elif l == 3:
			regData = "0"+regData

		if self.writer.write( comReg, regData ):
			return self.state
		
		raise IOError("AlarmAnswerException")
	
	#usa o bit 0 do registrador 9 para 
	#verificar se o alarme esta ligado ou desligado.
	#verifica se o alarme esta ligado ou desligado.
	#retorna true se o alarme estiver ligado
	#retorna false se o alarme estiver desligado
	def checkONOFF( self ):
		monitReg = "0009"
		regNumber = "0001"
		
		answer = self.reader.read( monitReg, regNumber )

		if answer[5]+answer[6] != "02":
			raise IOError("AlarmAnswerException")	

		regData = int( answer[7:11], 16 )

		return regData & 1 != 0
		
	
	#usa o bit 1 do registrador 9 para
	#verificar se o alarme esta disparado
	#se o mesmo esta disparado retorna true
	#senao false
	def fired( self ):	
		monitReg = "0009"
		regNumber = "0001"
		
		answer = self.reader.read(monitReg, regNumber)

		if answer[5]+answer[6] != "02":
			raise IOError("AlarmAnswerException")

		#fazer operacao logica em hexa em python
		#e uma droga porque ele fica adcionando
		#um 0x no inicio ai depois eu teria que tratar
		#la no calculo do checksum.
		return ( int( answer[7:11], 16 ) & 2 ) != 0

	def checkAlarm(self, place ):
		
		if self.monitRegBits.has_key( place ):
			monitReg = "000A"
			regNumber = "0001"

			answer = self.reader.read( monitReg, regNumber )
	
			if answer[5]+answer[6] != "02":
				raise IOError("AlarmAnswerException")

			regData = int( answer[7:11], 16 )

			return regData&( 1 << self.monitRegBits[place] ) != 0
			#montar mensagem e verificar
			#o status do alarm de um lugar em especifico
		else: 
			return None
 
		
