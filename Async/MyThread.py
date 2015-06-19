from threading import Thread
import time

class MyThread(Thread):

	def __init__(self, m ):
		Thread.__init__(self)
		self.monitor = m

	#como as thread iram fazer somente leitura
	#nao precisa controlar o sincronismo.
	def run(self):
		while True:
			self.monitor.myTurn()

			time.sleep(3)