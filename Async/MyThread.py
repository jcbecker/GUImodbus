from threading import Thread
import time

class MyThread(Thread):

	def __init__(self, m ):
		Thread.__init__(self)
		self.monitors = m

	def run(self):
		while True:
			for i in self.monitors:
				i.myTurn()
			time.sleep(5)
