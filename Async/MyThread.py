from threading import Thread
import time

class MyThread(Thread):

	def __init__(self, m ):
		Thread.__init__(self)
		self.monitors = m

	#como as thread iram fazer somente leitura
	#nao precisa controlar o sincronismo.
	def run(self):
		while True:
			for i in self.monitors:
				i.myTurn()
