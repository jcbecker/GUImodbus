#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from ..Resources.Alarm import Alarm
import Tkinter as tk
import Tkinter as tkk
import tkFont as font
import ttk
import threading
import time

from ..IO.ModBusWriter import ModBusWriter

class AlarmMonitor(tk.Frame,threading.Thread):

	def __init__(self, parent, controller ):
		tk.Frame.__init__(self,parent,background = "white")
		threading.Thread.__init__(self)

		self.user = Alarm()
		self.parent = parent
		self.ctrl = controller
		self.stopQuery = False
		self.exit = False

		self.xi=self.parent.winfo_x()
		self.yi=self.parent.winfo_y()

		self.buildTree()
		self.buildAlarmLabels()

	def buildTree(self):
		self.tree = ttk.Treeview(self.parent, columns=("Lugar","Estado"),
								selectmode="extended",height=5)
		self.tree["show"] = "headings"
		self.tree.heading("#1", text="Lugar", anchor="center" )
		self.tree.heading("#2", text="Estado", anchor="center")
		self.tree.column("#1", anchor="center", width=120)
		self.tree.column("#2", anchor="center", width=120)

		self.tree.place(
						x = self.xi+400,
						y = self.yi+160,
						width = self.xi+600,
						height = self.yi+350
						)

		p = []
		p.append("Garagem")
		p.append("Piscina 1")
		p.append("Cozinha")
		p.append("Sala de Estar")
		p.append("Sala de jogos")
		p.append("Suíte")
		p.append("Dormitório 1")
		p.append("Dormitório 2")

		for i in range(8):
			self.tree.insert("",i,text="", value=( p[i], " " ) )

		self.tID = self.tree.place_info()

		self.tree.place_forget()

	def buildAlarmLabels(self):
		self.ag = tk.Label(self.parent, text= " ", bg="white",
									font = font.Font(weight="normal",size=16))
		self.ag.place(x=self.xi+450,
					y=self.yi,
				 	width=self.xi+500,
					height=self.yi+50)

		self.agID = self.ag.place_info()
		self.ag.place_forget()

		self.ad = tk.Label(self.parent, text = " ", bg = "white",
						font = font.Font(weight="normal",size=16))

		self.ad.place(x=self.xi+450,
						y=self.yi+51,
						width=self.xi+500,
						height=self.yi+101)

		self.adID = self.ad.place_info()
		self.ad.place_forget()

	def hideWidgets(self):
		self.tree.place_forget()
		self.ag.place_forget()
		self.ad.place_forget()

	def showWidgets(self):
		self.ag.place(self.agID)
		self.ad.place(self.adID)
		self.tree.place(self.tID)

	def run(self):

		while not self.exit:
			flagFirst = True
			if not self.stopQuery:

				try:
					inf = self.user.alarmInf()
				except IOError as e:
					print "Exceção nos alarmes tentando ler novamente."
					inf = self.user.alarmInf()

				msg = "O alarme geral está "
				if inf[0]:
					msg = msg + "ligado."
				else:
					msg = msg + "desligado."

				self.ag["text"] = msg

				color = "red"
				msg = "O alarme"
				if not inf[1]:
					color = "white"
					msg = msg + " não"
				
				msg = msg + " está disparado."
				self.ad["text"] = msg

				states = inf[2]

				ch = self.tree.get_children()

				j = 0
				for i in ch:
					of = "OFF"
					if (states&(1 << j )) != 0:
						of = "ON"

					self.tree.set(i,1, of )

					j = j + 1

				if flagFirst:
					flagFirst = False
					self.showWidgets()

				#print "Monitor do alarme dormindo..."
				time.sleep(5)
			if not flagFirst:
				self.hideWidgets()
			#print "Monitor do alarme morto."