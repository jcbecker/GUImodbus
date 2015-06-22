#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from ..Resources.Lamp import Lamp
import Tkinter as tk
import tkFont as font
import threading
import ttk
import time

class LampMonitor(tk.Frame, threading.Thread):

	def __init__(self, parent, controller ):
		tk.Frame.__init__( self, parent)
		threading.Thread.__init__(self)

		self.user = Lamp()
		self.parent = parent
		self.ctrl = controller
		self.stopQuery = False
		self.exit = False

	def cleanBrothers(self):
		children = self.parent.winfo_children()
		for c in children:
			c.destroy()

	def run(self):
		self.xi1=self.parent.winfo_x()+50
		self.yi1=self.parent.winfo_y()-300
		self.xf1=2*self.parent.winfo_x()+300
		self.yf1=self.parent.winfo_y()+40

		while not self.exit:

			if self.stopQuery is False:
				self.cleanBrothers()

				try:
					self.state = self.user.monitLamps()
				except IOError as e:
					time.sleep(1)
					self.cleanBrothers()
					try:
						self.state = self.user.monitLamps()
					except IOError as e:
						pass

				self.lamp1()
				self.lamp2()
				self.lamp3()

				self.parent.update_idletasks()
		#		print "monitoramento das lampadas dormindo..."
				time.sleep(5)

		#print "monitor de lampadas morto."

	def lamp3(self):
		p = []
		p.append("BWC")
		p.append("Depósito")
		p.append("Varanda da piscina")
		p.append("Piscina 1")
		p.append("Piscina 2")
		p.append("Piscina 3")

		l = self.checkState(2)

		tree = ttk.Treeview(self.parent, columns=("lamp","state"),
							selectmode="extended",height=5)
		tree["show"] = "headings"
		tree.heading("#1", text="Lampadas 2", anchor="center" )
		tree.heading("#2", text="Estado", anchor="center")
		tree.column("#1", anchor="center", width=40)
		tree.column("#2", anchor="center", width=40)

		for i in range(6):
			tree.insert("",i,text="", value=( p[i], l[i] ) )

		tree.place(x=2*(self.xf1+self.xi1)+120,
					y=self.yi1,
					width=self.xf1+self.xi1+30,
					height=self.yf1)
	def lamp2(self):
		p = []
		p.append("BWC 1")
		p.append("Circulação")
		p.append("Dormitório 2")
		p.append("Closet")
		p.append("BWC 2")
		p.append("Suíte 1")
		p.append("Suíte 2")
		p.append("Suíte 3")

		l = self.checkState(1)

		tree = ttk.Treeview(self.parent, columns=("lamp","state"),
							selectmode="extended",height=5)
		tree["show"] = "headings"
		tree.heading("#1", text="Lampadas 2", anchor="center" )
		tree.heading("#2", text="Estado", anchor="center")
		tree.column("#1", anchor="center", width=40)
		tree.column("#2", anchor="center", width=40)

		for i in range(8):
			tree.insert("",i,text="", value=( p[i], l[i] ) )

		tree.place(x=self.xf1+90,
					y=self.yi1,
					width=self.xf1+self.xi1+30,
					height=self.yf1)

	def lamp1(self):
		p = []
		p.append("Sala de estar 1")
		p.append("Sala de estar 2")
		p.append("Sala de estar 3")
		p.append("Sala de jantar 1")
		p.append("Sala de jantar 2")
		p.append("Sala de jogos 1")
		p.append("Sala de jogos 2")
		p.append("Dormitório 1")

		l = self.checkState(0)

		tree = ttk.Treeview(self.parent, columns=("lamp","state"),
							selectmode="extended",height=5)
		tree["show"] = "headings"

		for i in range(8):
			tree.insert("",i,text="", value=( p[i], l[i] ) )

		tree.heading("#1", text="Lampadas 1", anchor="center" )
		tree.heading("#2", text="Estado", anchor="center")
		tree.column("#1", anchor="center", width=40)
		tree.column("#2", anchor="center", width=40)
		tree.place(x=self.xi1,
					y=self.yi1,
					width=self.xf1,
					height=self.yf1)

	def checkState(self,k):
		l = []
		stts = self.state[k]
		for i in range(8):	
			l.append("OFF")
			if ( stts & ( 1 << i ) ) != 0:
				l[i] = "ON"

		return l