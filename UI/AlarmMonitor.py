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
					onOFF = self.user.checkONOFF()
				except IOError as e:
					time.sleep(1)
					self.cleanBrothers()
					onOFF = self.user.checkONOFF()

				msg = "O alarme geral está "
				if onOFF:
					msg = msg + "ligado."
				else:
					msg = msg + "desligado."

				self.ag = tk.Label(self.parent, text= msg, bg="white",
									font = font.Font(weight="normal",size=16))
				self.ag.place(x=xi,
								y=yi-50,
						 		width=xf,
								height=yf-20)

				try:
					fired = self.user.fired()
				except IOError as e:
					time.sleep(1)
					onOFF = self.user.fired()

				color = "red"
				msg = "O alarme"
				if not fired:
					color = "white"
					msg = msg + " não"
				
				msg = msg + " está disparado."
				self.ad = tk.Label(self.parent, text = msg, bg = color,
									font = font.Font(weight="normal",size=16))
				self.ad.place(x=xi,
									y=yf-30,
									width=xf,
									height=yf-20)
				#ad.pack()
				tree = ttk.Treeview(self.parent, columns=("Lugar","Estado"),
									selectmode="extended",height=5)
				tree["show"] = "headings"
				tree.heading("#1", text="Lugar", anchor="center" )
				tree.heading("#2", text="Estado", anchor="center")
				tree.column("#1", anchor="center", width=120)
				tree.column("#2", anchor="center", width=120)

				try:
					states = self.user.checkAlarm()
				except IOError as e:
					time.sleep(1)
					try:
						states = self.user.checkAlarm()
					except IOError as e:
						pass

				p = []
				p.append("Garagem")
				p.append("Piscina 1")
				p.append("Cozinha")
				p.append("Sala de Estar")
				p.append("Sala de jogos")
				p.append("Suíte")
				p.append("Dormitório 1")
				p.append("Dormitório 2")

				canPlace = True
				for i in range(8):
					of = "OFF"
					if (states&(1 << i )) != 0:
						of = "ON"

					try:
						tree.insert("",i,text="", value=( p[i], of ) )
					except Exception as e:
						canPlace = False

				tree.place(
							x = xi,
							y = yf+20,
							width = xf,
							height = yf+250
							)
				self.parent.update_idletasks()
				#print "Monitor do alarme dormindo..."
				time.sleep(5)
			#print "Monitor do alarme morto."