from ..Resources.Temperature import Temperature
import Tkinter as tk
import tkFont as font
import threading
import time

class TemperatureMonitor(tk.Frame,threading.Thread):
			
	def __init__(self, parent, controller ):
		tk.Frame.__init__(self,parent,background = "white")
		threading.Thread.__init__(self)

		self.user = Temperature()
		self.parent = parent
		self.ctrl = controller
		self.stopQuery = False
			
	def run(self):
		while not self.stopQuery:
			children = self.parent.winfo_children()
			for widget in children:
				widget.destroy()

			l0 = tk.Label( self.parent, text = "Temperatura da Casa", font = font.Font(weight="normal",size=20), bg="white")
			l0.pack(side="top",fill="both",expand= True,ipady=30)

			l1 = tk.Label( self.parent, bg="white", font = font.Font(weight="normal",size=14) )
			l1.pack(side="top",fill="both",expand = True,ipady=25)

			l2 = tk.Label( self.parent, bg="white", font = font.Font(weight="normal",size=14) )
			l2.pack(side="top",fill="both",expand = True,ipady=25)

			l3 = tk.Label( self.parent, bg="white", font = font.Font(weight="normal",size=14) )
			l3.pack(side="top",fill="both",expand = True,ipady=25)

			l4 = tk.Label( self.parent, bg="white", font = font.Font(weight="normal",size=14) )
			l4.pack(side="top",fill="both",expand = True,ipady=25)

			l5 = tk.Label( self.parent, bg="white", font = font.Font(weight="normal",size=14) )
			l5.pack(side="top",fill="both",expand = True,ipady=25)

			l6 = tk.Label( self.parent, bg="white", font = font.Font(weight="normal",size=14) )
			l6.pack(side="top",fill="both",expand = True,ipady=25)		
			
			l7 = tk.Label( self.parent, bg="white", font = font.Font(weight="normal",size=14) )
			l7.pack(side="top",fill="both",expand = True,ipady=25)
			
			temps = self.user.readTemp()

			l1.configure( text = "Piscina: " + str( int( temps[0], 16 ) ) + " Graus", bg= "white" )
			l2.configure( text = "Banheira: " + str( int( temps[1], 16 ) ) + " Graus", bg= "white" )			
			l3.configure( text = "Suite: " + str( int( temps[2], 16 ) ) + " Graus", bg= "white" )
			l4.configure( text = "Sala de estar: " + str( int( temps[3], 16 ) ) + " Graus", bg= "white" )
			l5.configure( text = "Sala de jogos: " + str( int( temps[4], 16 ) ) + " Graus", bg= "white" )
			l6.configure( text = "Dormitorio 1: " + str( int( temps[5], 16 ) ) + " Graus", bg= "white" )
			l7.configure( text = "Dormitorio 2: " + str( int( temps[6], 16 ) ) + " Graus", bg= "white" )
			self.ctrl.update()
			print "monitor de temperatura dormindo.."
			time.sleep(2)