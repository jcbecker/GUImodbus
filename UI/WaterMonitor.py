#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..Resources.Water import Water
import Tkinter as tk
import Tkinter as tkk
import tkFont as font
import ttk
import threading
import time

from ..IO.ModBusWriter import ModBusWriter

class WaterMonitor(tk.Frame,threading.Thread):

	def __init__(self, parent, controller ):
		tk.Frame.__init__(self,parent,background = "white")
		threading.Thread.__init__(self)

		self.user = Water()
		self.parent = parent
		self.ctrl = controller
		self.stopQuery = False
		self.exit = False

		self.xi=self.parent.winfo_x()
		self.yi=self.parent.winfo_y()

		self.buildLevelLabel()
		self.buildTree()

	def buildLevelLabel(self):
		self.bathLevel = tk.Label(self.parent, text= " ", bg="white",
									font = font.Font(weight="normal",size=16))
				
		self.bathLevel.place(x=self.xi+410,
								y=self.yi,
				 				width=self.xi+500,
								height=self.yi+50)

		self.bathID = self.bathLevel.place_info()
		self.place_forget()

	def buildTree(self):
		self.tree = ttk.Treeview(self.parent, columns=("Lugar","Estado"),
									selectmode="extended",height=5)
		self.tree["show"] = "headings"
		self.tree.heading("#1", text="Lugar", anchor="center" )
		self.tree.heading("#2", text="Estado", anchor="center")
		self.tree.column("#1", anchor="center", width=120)
		self.tree.column("#2", anchor="center", width=120)	

		p = []
		p.append("Água quenta da banheira")
		p.append("Água fria da banheira")
		p.append("Água quenta da piscina")
		p.append("Água fria da banheira")

		for i in range(0,4):
			self.tree.insert("",i,text="", value=( p[i], " "))

		self.tree.place(x=self.xi+400,
						y=self.yi+51,
						width=self.xi+500,
						height=self.yi+200)

		self.tID = self.tree.place_info()
		self.tree.place_forget()

	def showWidgets(self):
		self.bathLevel.place( self.bathID )
		self.tree.place( self.tID )

	def hideWidgets(self):
		self.bathLevel.place_forget()
		self.tree.place_forget()

	def run(self):
		
		while not self.exit:
			if not self.stopQuery:
				try:
					inf = self.user.MonitWater()
				except IOError as e:
					print "Exceção na água tentando ler novamente."
					inf = self.user.MonitWater()

				msg = "Nivel d'água na banheira: " + str( inf[0] )
				self.bathLevel["text"] = msg
		
				try:
					ch = self.tree.get_children()
					j = 1
					for i in ch:
						of = "OFF"
						if inf[j]:
							of = "ON"
						self.tree.set( i, 1, of )
						j = j + 1

				except Exception as e:
					print "Exceção na construção do monitor da água."

				self.showWidgets()

				time.sleep(5)

			#print "Monitor da água durmindo.."
		#print "Monitor da água morto..."