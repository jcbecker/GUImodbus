from ..IO.ModBusReader import ModBusReader

class Temperature:
	
	def __init__(self):
		self.reader = ModBusReader()

	#le a temperatura de todos os lugares que possuem sensor.
	def readTemp(self):
		monitReg = "0000"
		regNumber = "0007"

		answer = self.reader.read(monitReg,regNumber)

		if answer[5]+answer[6] != "0E":
			raise IOError("WrongAnswerException")

		ini = 7
		end = 11
		temperatures = []
		for _ in range(7):
			temperatures.append( answer[ini:end] )
			ini = end
			end = end + 4

		return temperatures
