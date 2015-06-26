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
		self.notWrite = False

		self.xi=self.parent.winfo_x()
		self.yi=self.parent.winfo_y()

		self.buildWhiteBack()
		self.lamp1()
		self.lamp2()
		self.lamp3()
		self.buildObs()

	def hideWidgets(self):
		self.tree1.place_forget()
		self.tree2.place_forget()
		self.tree3.place_forget()
		self.obs1.place_forget()
		self.obs2.place_forget()
		self.obs3.place_forget()
		self.wb.place_forget()

	def showWidgets(self):
		self.tree1.place(self.t1ID)
		self.tree2.place(self.t2ID)
		self.tree3.place(self.t3ID)
		self.obs1.place(self.obs1ID)
		self.obs2.place(self.obs2ID)
		self.obs3.place(self.obs3ID)
		self.wb.place(self.wbID)

	def buildWhiteBack(self):
		self.wb = tk.Label(self.parent, text= " ", bg="white")

		self.wb.place(x=self.xi,
					  y=self.yi,
					  width=self.parent["width"],
					  height=self.parent["height"])
		self.wbID = self.wb.place_info()
		self.wb.place_forget()

	def buildObs(self):
		self.obs1 = tk.Label(self.parent, text= " ", bg="white",
									font = font.Font(weight="normal",size=16))

		self.obs1.place(x=self.xi+50,
								y=self.yi+345,
				 				width=300,
								height=50)

		self.obs1ID = self.obs1.place_info()
		self.obs1.place_forget()

		self.obs2 = tk.Label(self.parent, text= " ", bg="white",
									font = font.Font(weight="normal",size=16))

		self.obs2.place(x=self.xi+440,
							y=self.yi+345,
							width=300,
							height=50)

		self.obs2ID = self.obs2.place_info()
		self.obs2.place_forget()

		self.obs3 = tk.Label(self.parent, text= " ", bg="white",
									font = font.Font(weight="normal",size=16))

		self.obs3.place(x=self.xi+850,
							y=self.yi+295,
							width=350,
							height=50)

		self.obs3ID = self.obs3.place_info()
		self.obs3.place_forget()

	def lampListener1(self,e):
		i = self.tree1.identify('item',e.x,e.y)
		self.switchLamp("000E",i,self.tree1,self.chTree1,self.obs1)

	def lampListener2(self,e):
		i = self.tree2.identify('item',e.x,e.y)
		self.switchLamp("000F",i,self.tree2,self.chTree2,self.obs2)

	def lampListener3(self,e):
		i = self.tree3.identify('item',e.x,e.y)
		self.switchLamp("0010",i,self.tree3,self.chTree3,self.obs3)

	def switchLamp(self,reg,i,tree,chTree,obs):
		
		if self.notWrite:
			obs["bg"] = "#CC3300"
			return None

		chi = int( str(i)[1:] )-1
		hardware = 0 			
		while hardware < 1000:
			try:
				of = "OFF"
				if self.user.switch(reg,chi):
					of = "ON"

				tree.set( chTree[chi], 1, of )
				obs["bg"] = "white"
				break;
			except Exception as e:
				#print str(hardware)
				hardware = hardware + 1
				time.sleep(0.5)
			#print "Exceção na mudança do estado da torneira tente novamente"

		if hardware == 1000:
			obs["bg"] = "white"
			obs["text"] = "Erro no hardware da torneira."

	def run(self):

		while not self.exit:
			flagFirst = True
			if self.stopQuery is False:

				try:
					self.notWrite = True
					self.state = self.user.monitLamps()

					self.checkState(0,self.tree1,self.chTree1)
					self.checkState(1,self.tree2,self.chTree2)
					self.checkState(2,self.tree3,self.chTree3)

					if flagFirst:
						flagFirst = False
						self.showWidgets()

					if self.exit:
						break
				
					self.notWrite = False
					#print "Monito das lampadas durmindo."
					
					time.sleep(5)
				except IOError as e:
					print "Exceção nas lampadas aguarde outra leitura."

			if (not flagFirst) and self.stopQuery:
				self.hideWidgets()			
		#print "Monitor das lampadas morto."

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

		self.tree3.place(x=self.xi+850,
							y=self.yi,
							width=350,
							height=290)

		self.chTree3 = self.tree3.get_children()
		self.t3ID = self.tree3.place_info()
		self.tree3.bind("<Button-1>", self.lampListener3)
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

		self.tree2.place(x=self.xi+440,
							y=self.yi,
							width=300,
							height=340)

		self.chTree2 = self.tree2.get_children()
		self.t2ID = self.tree2.place_info()
		self.tree2.bind("<Button-1>", self.lampListener2)
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
							height=340)

		self.chTree1 = self.tree1.get_children()
		self.t1ID = self.tree1.place_info()
		self.tree1.bind("<Button-1>", self.lampListener1)
		self.tree1.place_forget()

	def checkState(self,k,tree,ch):
		
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