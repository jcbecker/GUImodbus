from threading import Thread
import time

class MyThread(Thread):

	def __init__(self, name, ctrl ):
		Thread.__init__(self)
		self.tName = name
		self.ctrl = ctrl

	def run(self):
		while True:
			self.ctrl.myTurn()

			time.sleep(3)