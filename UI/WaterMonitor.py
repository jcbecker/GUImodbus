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
		self.buildExhaustBath()
		self.buildTree()

	def exhaustBath(self):
		try:
			self.user.tap(3)
		except IOError as e:
			self.user.tap(3)

	def buildExhaustBath(self):
		self.exhaust = tk.Button( self.parent, text = "Esvaziar", fg="white", 
									font = font.Font(weight="normal",size=14), 
									bg="#0099CC", 
									activebackground="white",
									command= self.exhaustBath )

		self.exhaust.place(x=self.xi+725,
							y=self.yi,
							width=175,
							height=self.yi+50)

		self.exhaustID = self.exhaust.place_info()
		self.exhaust.place_forget()

	def buildLevelLabel(self):
		self.bathLevel = tk.Label(self.parent, text= " ", bg="white",
									font = font.Font(weight="normal",size=16))
				
		self.bathLevel.place(x=self.xi+400,
								y=self.yi,
				 				width=320,
								height=self.yi+50)

		self.bathID = self.bathLevel.place_info()
		self.bathLevel.place_forget()

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
		p.append("Água fria da piscina")

		for i in range(0,4):
			self.tree.insert("",i,text="", value=( p[i], " "))

		self.tree.place(x=self.xi+400,
						y=self.yi+51,
						width=self.xi+500,
						height=self.yi+200)

		self.tree.bind("<Button-1>", self.waterListener)
		self.chTree = self.tree.get_children()
		self.tID = self.tree.place_info()
		self.tree.place_forget()

	def waterListener(self, e ):

		i = self.tree.identify('item',e.x,e.y)
		chi = int( str(i)[1:] )

		k = chi
		if k >= 3:
			k = k + 1

		hardware = 0
		while hardware < 1000:
			try:
				of = "OFF"
				if self.user.tap(k):
					of = "ON"

				self.tree.set( self.chTree[chi-1], 1, of )

				break;
			except Exception as e:
				hardware = hardware + 1
				print "Exceção na mudança do estado da torneira tente novamente"

		if hardware == 1000:
			print "Hardware problem!"	

	def showWidgets(self):
		self.bathLevel.place( self.bathID )
		self.tree.place( self.tID )
		self.exhaust.place(self.exhaustID)

	def hideWidgets(self):
		self.bathLevel.place_forget()
		self.exhaust.place_forget()
		self.tree.place_forget()

	def run(self):
		
		while not self.exit:
			flagFirst = True
			if not self.stopQuery:

				try:
					inf = self.user.MonitWater()
					msg = "Nivel d'água na banheira: " + str( inf[0] )
					self.bathLevel["text"] = msg
						
					j = 1
					for i in self.chTree:
						of = "OFF"
						if inf[j]:
							of = "ON"
						self.tree.set( i, 1, of )
						j = j + 1

					if flagFirst:
						flagFirst = False
						self.showWidgets()

					if self.exit:
						break
					time.sleep(5)

					print "Monitor da água durmindo.."
				except Exception as e:

					print "Exceção na água aguarde outra leitura."


			if (not flagFirst) and self.stopQuery:
				self.hideWidgets()
		#print "Monitor da água morto..."