from Monitor import Monitor

class LampMonitor(Monitor):

	def myTurn(self):

		k = 0
		for i in self.user.monitLamps():
			print str(k) + " " + str(i)
			k = k + 1
