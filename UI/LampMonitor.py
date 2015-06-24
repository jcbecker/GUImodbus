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

		self.xi=self.parent.winfo_x()
		self.yi=self.parent.winfo_y()

		self.lamp1()
		self.lamp2()
		self.lamp3()

	def hideWidgets(self):
		self.tree1.place_forget()
		self.tree2.place_forget()
		self.tree3.place_forget()

	def showWidgets(self):
		self.tree1.place(self.t1ID)
		self.tree2.place(self.t2ID)
		self.tree3.place(self.t3ID)

	def run(self):
		
		while not self.exit:
			flagFirst = True
			if self.stopQuery is False:

				try:
					self.state = self.user.monitLamps()
				except IOError as e:
					print "Exceção nas lampadas tentando ler novamente."
					self.state = self.user.monitLamps()

				self.checkState(0,self.tree1)
				self.checkState(1,self.tree2)
				self.checkState(2,self.tree3)

				if flagFirst:
					flagFirst = False
					self.showWidgets()
				
				time.sleep(5)

	def lamp3(self):
		p = []
		p.append("BWC")
		p.append("Depósito")
		p.append("Varanda da piscina")
		p.append("Piscina 1")
		p.append("Piscina 2")
		p.append("Piscina 3")

		self.tree3 = self.newTree(3)

		for i in range(6):
			self.tree3.insert("",i,text="", value=( p[i], " " ) )

		self.tree3.place(x=self.xi+800,
							y=self.yi,
							width=350,
							height=self.yi+300)

		self.t3ID = self.tree3.place_info()
		self.tree3.place_forget()

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

		self.tree2 = self.newTree(2)

		for i in range(8):
			self.tree2.insert("",i,text="", value=( p[i], " " ) )

		self.tree2.place(x=self.xi+400,
							y=self.yi,
							width=300,
							height=self.yi+300)

		self.t2ID = self.tree2.place_info()
		self.tree2.place_forget()

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

		self.tree1 = self.newTree(1)

		for i in range(8):
			self.tree1.insert("",i,text="", value=( p[i], " " ) )

		self.tree1.place(x=self.xi+50,
							y=self.yi,
							width=300,
							height=self.yi+300)

		self.t1ID = self.tree1.place_info()
		self.tree1.place_forget()

	def checkState(self,k,tree):
		ch = tree.get_children()
		
		j = 0
		stts = self.state[k]
		for i in ch:	
			of = "OFF"
			
			if ( stts & ( 1 << j ) ) != 0:
				of = "ON"

			tree.set(i,1, of )
			j = j + 1

	def newTree(self,id):
		tree = ttk.Treeview(self.parent, columns=("lamp","state"),
							selectmode="extended",height=5)
		tree["show"] = "headings"
		tree.heading("#1", text="Lampadas "+str(id), anchor="center" )
		tree.heading("#2", text="Estado", anchor="center")
		tree.column("#1", anchor="center", width=40)
		tree.column("#2", anchor="center", width=40)

		return tree