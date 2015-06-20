from ..Resources.Temperature import Temperature
import Tkinter as tk
import tkFont as font
import threading
import time

class TemperatureMonitor(tk.Frame, threading.Thread):
			
	def __init__(self, parent, controller ):
		tk.Frame.__init__(self,parent)
		threading.Thread.__init__(self)

		self.user = Temperature()
		self.start()
			
	def run(self):
		l0 = tk.Label( self, text = "Temperatura da Casa", font = font.Font(weight="normal",size=20), bg="white")
		l0.pack(side="top",fill="both",expand= True)

		l1 = tk.Label( self )
		l1.pack(side="top",fill="both",expand = True)

		l2 = tk.Label( self )
		l2.pack(side="top",fill="both",expand = True)

		l3 = tk.Label( self )
		l3.pack(side="top",fill="both",expand = True)

		l4 = tk.Label( self )
		l4.pack(side="top",fill="both",expand = True)

		l5 = tk.Label( self )
		l5.pack(side="top",fill="both",expand = True)

		l6 = tk.Label( self )
		l6.pack(side="top",fill="both",expand = True)		
		
		l7 = tk.Label( self )
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

			self.update()

			time.sleep(1)