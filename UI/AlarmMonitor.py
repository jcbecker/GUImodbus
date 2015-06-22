#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from ..Resources.Alarm import Alarm
import Tkinter as tk
import Tkinter as tkk
import tkFont as font
import ttk
import threading
import time

class AlarmMonitor(tk.Frame,threading.Thread):

	def __init__(self, parent, controller ):
		tk.Frame.__init__(self,parent,background = "white")
		threading.Thread.__init__(self)

		self.user = Alarm()
		self.parent = parent
		self.ctrl = controller
		self.stopQuery = False
		self.exit = False

	def cleanBrothers(self):
		children = self.parent.winfo_children()
		for c in children:
			c.destroy()

	def run(self):

		xi=self.parent.winfo_x()+400
		yi=self.parent.winfo_y()-300
		xf=2*self.parent.winfo_x()+550
		yf=self.parent.winfo_y()-250
		while not self.exit:

			if not self.stopQuery:
				self.cleanBrothers()

				try:
					inf = self.user.alarmInf()
				except IOError as e:
					time.sleep(1)
					self.cleanBrothers()
					inf = self.user.alarmInf()

				msg = "O alarme geral está "
				if inf[0]:
					msg = msg + "ligado."
				else:
					msg = msg + "desligado."

				ag = tk.Label(self.parent, text= msg, bg="white",
									font = font.Font(weight="normal",size=16))
				ag.place(x=xi,
							y=yi-50,
						 	width=xf,
							height=yf-20)

				color = "red"
				msg = "O alarme"
				if not inf[1]:
					color = "white"
					msg = msg + " não"
				
				msg = msg + " está disparado."
				ad = tk.Label(self.parent, text = msg, bg = color,
									font = font.Font(weight="normal",size=16))
				ad.place(x=xi,
							y=yf-30,
							width=xf,
							height=yf-20)
				
				tree = ttk.Treeview(self.parent, columns=("Lugar","Estado"),
									selectmode="extended",height=5)
				tree["show"] = "headings"
				tree.heading("#1", text="Lugar", anchor="center" )
				tree.heading("#2", text="Estado", anchor="center")
				tree.column("#1", anchor="center", width=120)
				tree.column("#2", anchor="center", width=120)

				p = []
				p.append("Garagem")
				p.append("Piscina 1")
				p.append("Cozinha")
				p.append("Sala de Estar")
				p.append("Sala de jogos")
				p.append("Suíte")
				p.append("Dormitório 1")
				p.append("Dormitório 2")

				try:
					states = inf[2]
					for i in range(8):
						of = "OFF"
						if (states&(1 << i )) != 0:
							of = "ON"

						tree.insert("",i,text="", value=( p[i], of ) )

					tree.place(
								x = xi,
								y = yf+20,
								width = xf,
								height = yf+250
								)

					self.parent.update_idletasks()
				except Exception as e:
					pass

				#print "Monitor do alarme dormindo..."
				time.sleep(5)
			#print "Monitor do alarme morto."