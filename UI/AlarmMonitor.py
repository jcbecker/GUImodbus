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
		self.notWrite = False

		self.xi=self.parent.winfo_x()
		self.yi=self.parent.winfo_y()

		self.buildWhiteBack()
		self.buildTree()
		self.buildAlarmLabels()
		self.buildButtons()
		self.obsLabel()

	def hideWidgets(self):
		self.tree.place_forget()
		self.ag.place_forget()
		self.ad.place_forget()
		self.onOff.place_forget()
		self.obs.place_forget()
		self.wb.place_forget()

	def showWidgets(self):
		self.ag.place(self.agID)
		self.ad.place(self.adID)
		self.onOff.place(self.onOffID)
		self.tree.place(self.tID)
		self.obs.place(self.obsID)
		self.wb.place(self.wbID)

	def buildWhiteBack(self):
		self.wb = tk.Label(self.parent, text= " ", bg="white")

		self.wb.place(x=self.xi,
					  y=self.yi,
					  width=self.parent["width"],
					  height=self.parent["height"])
		self.wbID = self.wb.place_info()
		self.wb.place_forget()

	def obsLabel(self):

		self.obs = tk.Label(self.parent, text= " ", bg="white",
									font = font.Font(weight="normal",size=16))
				
		self.obs.place(x=self.xi+400,
								y=self.yi+460,
				 				width=500,
								height=50)

		self.obsID = self.obs.place_info()
		self.obs.place_forget()

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

		if self.notWrite:
			self.obs["bg"] = "#CC3300"
			return None
		
		hardware = 0
		while hardware < 1000:
			try:
				if self.user.ONOFF():
					self.onOff["bg"] = "#CC3300"
					self.onOff["text"] = "Desligar"
				else:
					self.onOff["bg"] = "#339966"
					self.onOff["text"] = "Ligar"

					self.obs["bg"] = "white"
				break;
			except Exception as e:
				hardware = hardware + 1

		if hardware == 1000:
			self.obs["bg"] = "white"
			self.obs["text"] = "Error no hardware do alarme."

	def buildButtons(self):
		self.onOff = tk.Button( self.parent, text = "Ligar", fg="white", 
								font = font.Font(weight="normal",size=14),
								bg="#339966", 
								activebackground="white",
								command= self.ONOFFListener )

		self.onOff.place(x=self.xi+735,
							y=self.yi+41,
							width=165,
							height=51
						)

		self.onOffID = self.onOff.place_info()
		self.onOff.place_forget()

	def buildAlarmLabels(self):
		self.ag = tk.Label(self.parent, text= " ", bg="white",
							font = font.Font(weight="normal",size=16))

		self.ag.place(x=self.xi+400,
						y=self.yi+50,
						width=330,
						height=30)

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
					self.notWrite = True
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

					if flagFirst and (not self.stopQuery):
						flagFirst = False
						self.showWidgets()

					if self.exit:
						break

					self.notWrite = False
					#print "Monitor do alarme dormindo..."
					
					time.sleep(5)
				except Exception as e:
					pass
		#			print "Exceção nos alarmes aguarde outra leitura."
					

			if (not flagFirst) and self.stopQuery:
				self.hideWidgets()
		#print "Monitor do alarme morto."
