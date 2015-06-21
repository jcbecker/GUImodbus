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

	def run(self):

		xi=self.parent.winfo_x()+400
		yi=self.parent.winfo_y()-300
		xf=2*self.parent.winfo_x()+550
		yf=self.parent.winfo_y()-100
		while not self.exit:

			if not self.stopQuery:
				children = self.parent.winfo_children()
				for c in children:
					c.destroy()

				msg = "O alarme geral está "
				if self.user.checkONOFF():
					msg = msg + "ligado."
				else:
					msg = msg + "desligado."

				self.ag = tk.Label(self.parent, text= msg, bg="red",
									font = font.Font(weight="normal",size=16))
				self.ag.place(x=xi,
								y=yi,
						 		width=xf,
								height=yf)
				#ag.pack()
				msg = "O alarme"
				if not self.user.fired():
					msg = msg + " não"
				
				msg = msg + " está disparado."
				self.ad = tk.Label(self.parent, text = msg,
									font = font.Font(weight="normal",size=16))
				self.ad.place(x=xi,
									y=yf+50,
									width=xf+100,
									height=yf+50)
				#ad.pack()
				tree = ttk.Treeview(self.parent, columns=("Lugar","Estado"),
									selectmode="extended",height=5)
				tree["show"] = "headings"
				tree.heading("#1", text="Lugar", anchor="center" )
				tree.heading("#2", text="Estado", anchor="center")
				tree.column("#1", anchor="center", width=120)
				tree.column("#2", anchor="center", width=120)



				self.parent.update_idletasks()
				#print "Monitor do alarme dormindo..."
				time.sleep(5)
			#print "Monitor do alarme morto."