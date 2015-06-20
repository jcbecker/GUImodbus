from ..Resources.Temperature import Temperature
from Tkinter import *
import threading
import time

class TemperatureMonitor(threading.Thread):
			
	def __init__(self):
		self.user = Temperature()
			
	def event(self, w):
		self.run()
			
	def close(self):
		threading.Event().set()
			
	def run(self):
		
		self.tempView = Tk()
		self.tempView.wm_title("Temperaturas da Casa")
		self.tempView.geometry("350x350")   
		self.tempView.protocol("WM_DELETE_WINDOW", self.close() )
		self.monitoring = Label( self.tempView ) 
		self.monitoring.place(x=0,
							  y=0,
							  width=350,
							  height=350)
	
		while True:
			temps = self.user.readTemp()
			
			t = "Pscina: " + str( temps[0] ) + " Graus\n"
			t += "Banheira: " + str( temps[1] ) + " Graus\n"
			t += "Suite: " + str( temps[2] ) + " Graus\n"
			t += "Sala de estar: " + str( temps[3] ) + " Graus\n"
			t += "Sala de jogos: " + str( temps[4] ) + " Graus\n"
			t += "Dormitorio 1: " + str( temps[5] ) + " Graus\n" 
			t += "Dormitorio 2: " + str( temps[6] ) + " Graus\n"
				
			self.monitoring.config(text=t )	
			self.tempView.update()
				
