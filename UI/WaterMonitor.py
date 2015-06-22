#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..Resources.Water import Water
import Tkinter as tk
import Tkinter as tkk
import tkFont as font
import ttk
import threading
import time

class WaterMonitor(tk.Frame,threading.Thread):

	def __init__(self, parent, controller ):
		tk.Frame.__init__(self,parent,background = "white")
		threading.Thread.__init__(self)

		self.user = Water()
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
					inf = self.user.MonitWater()
				except IOError as e:
					time.sleep(1)
					self.cleanBrothers()
					inf = self.user.MonitWater()

				msg = "Nivel d'água na banheira: " + str( inf[0] )

				bathLevel = tk.Label(self.parent, text= msg, bg="white",
									font = font.Font(weight="normal",size=16))
				
				bathLevel.place(x=xi,
								y=yi-50,
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
				p.append("Água quenta da banheira")
				p.append("Água fria da banheira")
				p.append("Água quenta da piscina")
				p.append("Água fria da banheira")		

				try:
					for i in range(0,4):
						of = "OFF"
						if inf[i+1]:
							of = "ON"

						tree.insert("",i,text="", value=( p[i], of ) )

					tree.place(
								x = xi,
								y = yf+20,
								width = xf,
								height = yf+150
								)

					self.parent.update_idletasks()
				except Exception as e:
					pass
			#print "Monitor da água durmindo.."
			time.sleep(5)
		#print "Monitor da água morto..."