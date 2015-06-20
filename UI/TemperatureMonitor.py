from ..Resources.Temperature import Temperature
from Tkinter import *
import threading
import time

class TemperatureMonitor(threading.Thread):
			
	def __init__(self, sW, sH ):
		self.user = Temperature()
		self.sW = sW
		self.sH = sH

	def event(self, w):
		self.run()
			
	def close(self):
		threading.Event().set()
			
	def run(self):
		
		self.tempView = Tk()
		self.tempView.wm_title("Temperaturas da Casa")
		self.tempView.geometry("380x380")   
		self.tempView.protocol("WM_DELETE_WINDOW", self.close() )
		self.tempView.configure(background="white")
	
		l1 = Label( self.tempView )
		l1.pack(side="top",fill="both",expand = True)

		l2 = Label( self.tempView )
		l2.pack(side="top",fill="both",expand = True)

		l3 = Label( self.tempView )
		l3.pack(side="top",fill="both",expand = True)

		l4 = Label( self.tempView )
		l4.pack(side="top",fill="both",expand = True)

		l5 = Label( self.tempView )
		l5.pack(side="top",fill="both",expand = True)

		l6 = Label( self.tempView )
		l6.pack(side="top",fill="both",expand = True)		
		
		l7 = Label( self.tempView )
		l7.pack(side="top",fill="both",expand = True)

		#se sobrar tempo arrumar um sistema de cores.
		while True:
			temps = self.user.readTemp()
			

			l1.configure( text = "Piscina: " + str( int( temps[0], 16 ) ) + " Graus", bg= "white" )
			l2.configure( text = "Banheira: " + str( int( temps[1], 16 ) ) + " Graus", bg= "white" )			
			l3.configure( text = "Suite: " + str( int( temps[2], 16 ) ) + " Graus", bg= "white" )
			l4.configure( text = "Sala de estar: " + str( int( temps[3], 16 ) ) + " Graus", bg= "white" )
			l5.configure( text = "Sala de jogos: " + str( int( temps[4], 16 ) ) + " Graus", bg= "white" )
			l6.configure( text = "Dormitorio 1: " + str( int( temps[5], 16 ) ) + " Graus", bg= "white" )
			l7.configure( text = "Dormitorio 2: " + str( int( temps[6], 16 ) ) + " Graus", bg= "white" )

			
			self.tempView.update()