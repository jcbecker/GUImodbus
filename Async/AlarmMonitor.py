from Monitor import Monitor

class AlarmMonitor(Monitor):

	def myTurn(self):

		if self.user.fired():
			print "O alarme esta disparado."