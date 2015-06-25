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
		self.writer = ModBusWriter()
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
		self.buildButtons()

	def hideWidgets(self):
		self.tree.place_forget()
		self.ag.place_forget()
		self.ad.place_forget()
		self.onOff.place_forget()

	def showWidgets(self):
		self.ag.place(self.agID)
		self.ad.place(self.adID)
		self.onOff.place(self.onOffID)
		self.tree.place(self.tID)

	def buildTree(self):
		self.tree = ttk.Treeview(self.parent, columns=("Lugar","Estado"),
									selectmode="extended",height=5)
		self.tree["show"] = "headings"
		self.tree.heading("#1", text="Lugar", anchor="center" )
		self.tree.heading("#2", text="Estado", anchor="center")
		self.tree.column("#1", anchor="center", width=100)
		self.tree.column("#2", anchor="center", width=100)

		self.tree.place(
						x = self.xi+400,
						y = self.yi+100,
						width = 500,
						height = 350
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

		#importante para não criar muitas listas.
		self.chTree = self.tree.get_children()
		self.tID = self.tree.place_info()

		self.tree.place_forget()

	#funciona mas para testar realmente
	#tem que mudar o valor dos registradores
	#de monitoramento.
	def ONOFFListener(self):
		
		hardware = 0
		while hardware < 1000:
			try:
				if self.user.ONOFF():
					self.onOff["bg"] = "#CC3300"
					self.onOff["text"] = "Desligar"
				else:
					self.onOff["bg"] = "#339966"
					self.onOff["text"] = "Ligar"

				break;
			except Exception as e:
				hardware = hardware + 1
				#print "Exceção enquanto ligava/desligava alarme."

		if hardware == 1000:
			print "hardware problem!"

	def buildButtons(self):
		self.onOff = tk.Button( self.parent, text = "Ligar", fg="white", 
								font = font.Font(weight="normal",size=14),
								bg="#339966", 
								activebackground="white",
								command= self.ONOFFListener )

		self.onOff.place(x=self.xi+705,
							y=self.yi+41,
							width=195,
							height=51
						)

		self.onOffID = self.onOff.place_info()
		self.onOff.place_forget()

	def buildAlarmLabels(self):
		self.ag = tk.Label(self.parent, text= " ", bg="white",
							font = font.Font(weight="normal",size=16))

		self.ag.place(x=self.xi+400,
						y=self.yi+50,
						width=320,
						height=20)

		self.agID = self.ag.place_info()
		self.ag.place_forget()

		self.ad = tk.Label(self.parent, text = " ", bg = "white",
							font = font.Font(weight="normal",size=16))

		self.ad.place(x=self.xi+400,
						y=self.yi+10,
				 		width=320,
						height=20)
		self.adID = self.ad.place_info()
		self.ad.place_forget()

	def run(self):

		while not self.exit:
			flagFirst = True
			if not self.stopQuery:

				try:
					self.inf = self.user.alarmInf()
					msg = "O alarme geral está "
					if self.inf[0]:
						self.onOff["bg"] = "#CC3300"
						self.onOff["text"] = "Desligar"
						msg = msg + "ligado."
					else:
						self.onOff["bg"] = "#339966"
						self.onOff["text"] = "Ligar"
						msg = msg + "desligado."

					self.ag["text"] = msg

					color = "red"
					msg = "O alarme"
					if not self.inf[1]:
						color = "white"
						msg = msg + " não"
					
					msg = msg + " está disparado."
					self.ad["text"] = msg

					states = self.inf[2]

					j = 0
					for i in self.chTree:
						of = "OFF"
						if (states&(1 << j )) != 0:
							of = "ON"

						self.tree.set(i,1, of )

						j = j + 1

					if flagFirst:
						flagFirst = False
						self.showWidgets()

					if self.exit:
						break

					#print "Monitor do alarme dormindo..."
					time.sleep(5)
				except Exception as e:
					pass
		#			print "Exceção nos alarmes aguarde outra leitura."
					

			if (not flagFirst) and self.stopQuery:
				self.hideWidgets()
		#print "Monitor do alarme morto."