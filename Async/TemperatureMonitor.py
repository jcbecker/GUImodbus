from Monitor import Monitor

class TemperatureMonitor(Monitor):

	def myTurn(self):

		k = 0
		for i in self.user.readTemp():
			print str(k) + " " + i
			k = k + 1
