#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from ..Resources.Temperature import Temperature
import Tkinter as tk
import Tkinter as tkk
import tkFont as font
import ttk
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
		self.exit = False
			
	def run(self):
		
		xi=self.parent.winfo_x()+300
		yi=self.parent.winfo_y()-300
		xf=2*self.parent.winfo_x()+700
		yf=self.parent.winfo_y()+40
		while not self.exit:
			if not self.stopQuery:
				children = self.parent.winfo_children()
				for widget in children:
					widget.destroy()

				temps = self.user.readTemp()
				tree = ttk.Treeview(self.parent, columns=("Lugar","Temperatura"),
									selectmode="extended",height=5)
				tree["show"] = "headings"
				tree.heading("#1", text="Lugar", anchor="center" )
				tree.heading("#2", text="Temperatura", anchor="center")
				tree.column("#1", anchor="center", width=120)
				tree.column("#2", anchor="center", width=120)

				tree.insert("",0,text="", 
							value=( "Piscina", str( int( temps[0], 16 ) ) + "°C" ) ) 
				tree.insert("",1,text="", 
							value=( "Banheira", str( int( temps[1], 16 ) ) + "°C") ) 
				tree.insert("",2,text="", 
							value=( "Suite", str( int( temps[2], 16 ) ) + "°C") ) 
				tree.insert("",3,text="", 
							value=( "Sala de estar", str( int( temps[3], 16 ) ) + "°C" ) ) 
				tree.insert("",4,text="", 
							value=( "Sala de jogos", str( int( temps[4], 16 ) ) + "°C" ) ) 
				tree.insert("",5,text="", 
							value=( "Dormitorio 1", str( int( temps[5], 16 ) ) + "°C" ) ) 
				tree.insert("",6,text="", 
							value=( "Dormitorio 2", str( int( temps[6], 16 ) ) + "°C" ) ) 
				tree.place(	x=xi, y=yi,
							width= xf, height= yf )

				self.parent.update_idletasks()
		#		print "monitor de temperatura dormindo.."
				time.sleep(5)
		#print "monitor de temperatura morto."