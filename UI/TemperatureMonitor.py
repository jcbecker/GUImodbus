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

		self.xi=self.parent.winfo_x()
		self.yi=self.parent.winfo_y()

		self.buildTree()

	def hideWidgets(self):
		self.tree.place_forget()

	def showWidgets(self):
		self.tree.place(self.tID)

	def run(self):

		while not self.exit:
			flagFirst = True
			if not self.stopQuery:

				try:	
					temps = self.user.readTemp()
				except IOError as e:
					temps = self.user.readTemp()

				ch = self.tree.get_children()

				j = 0
				for i in ch:
					self.tree.set(i,1, str( int(temps[j],16) )+"°C" )
					j = j + 1

				if flagFirst:
					flagFirst = False
					self.showWidgets()

				#print "monitor de temperatura dormindo.."
				time.sleep(5)
				
			if not flagFirst:
				self.hideWidgets()
		#print "monitor de temperatura morto."

	def buildTree(self):
		self.tree = ttk.Treeview(self.parent, columns=("Lugar","Temperatura"),
									selectmode="extended",height=5)
		self.tree["show"] = "headings"
		self.tree.heading("#1", text="Lugar", anchor="center" )
		self.tree.heading("#2", text="Temperatura", anchor="center")
		self.tree.column("#1", anchor="center", width=120)
		self.tree.column("#2", anchor="center", width=120)

		p = []
		p.append("Piscina")
		p.append("Banheira")
		p.append("Suite")
		p.append("Sala de estar")
		p.append("Sala de jogos")
		p.append("Dormitório 1")
		p.append("Dormitório 2")

		for i in range(7):
			self.tree.insert("",0,text="", 
							value=( p[i], " " ) ) 

		self.tree.place(x=self.xi+500,
						y=self.yi+51,
						width=300,
						height=self.yi+300)

		self.tID = self.tree.place_info()
		self.tree.place_forget()