#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from ..IO.ModBusWriter import ModBusWriter
from TemperatureMonitor import TemperatureMonitor 
from WaterMonitor import WaterMonitor
from AlarmMonitor import AlarmMonitor
from LampMonitor import LampMonitor

import tkFont as font
import Tkinter as tk
import ttk
import threading
import time

class Main(tk.Tk):

	def __init__( self ):
		tk.Tk.__init__(self)
		self.screenWidth = self.winfo_screenwidth()-10
		self.screenHeight = self.winfo_screenheight()-10

		self.geometry(str(self.screenWidth)+"x"+str(self.screenHeight))
		self.wm_title("Controle da casa")
		self.configure(background="white")
		self.protocol('WM_DELETE_WINDOW', self.quit) 

		#distancia entre linhas.
		self.distBetweenLines = self.screenHeight*0.01

		#distancia entre botoes na segunda linha.
		self.distBetweenBtnSecLine = self.screenWidth*0.04

		#distancia entre botoes na quarta linha.
		self.distBetweenBtnFourthLine = self.screenWidth*0.1
		self.labelHeight = 0.07*self.screenHeight

		self.labelFont = font.Font(weight="normal",size=20)
		self.btnFont = font.Font(weight="normal",size=14)

		self.line1()
		self.line2()

		style = ttk.Style(self)
		style.configure('Treeview', rowheight=40, font = font.Font(weight="normal",size=16))

		self.actions = tk.Frame(height = self.screenHeight*0.75,width=self.screenWidth,bg="white")
		self.actions.pack(side="bottom", fill="x", expand = False)
		self.actions.grid_rowconfigure(0,weight=1)		
		self.actions.grid_columnconfigure(0,weight=1)

		self.showing = None
		self.tempMonitor = TemperatureMonitor(self.actions,self)
		self.waterMonitor = WaterMonitor(self.actions,self)
		self.alarmMonitor = AlarmMonitor(self.actions,self)
		self.lampMonitor = LampMonitor(self.actions,self)

	def quit(self):
		self.alarmMonitor.exit = True
		self.waterMonitor.exit = True
		self.tempMonitor.exit = True
		self.lampMonitor.exit = True
		if self.alarmMonitor.isAlive():
			self.alarmMonitor.join(1)

		if self.waterMonitor.isAlive():
			self.waterMonitor.join(1)

		if self.tempMonitor.isAlive():
			self.tempMonitor.join(1)

		if self.lampMonitor.isAlive():
			self.lampMonitor.join(1)
		self.destroy()

	def stopCurrent(self):
		if self.showing is not None:
			self.showing.hideWidgets()
			self.showing.stopQuery = True

	def showTempMonitor(self):
		if self.showing != self.tempMonitor:
			self.stopCurrent()

			self.showing = self.tempMonitor
			self.tempMonitor.stopQuery = False
			if not self.tempMonitor.isAlive():
				self.tempMonitor.start()

	def showLampMonitor(self):
		if self.showing != self.lampMonitor:
			self.stopCurrent()

			self.showing = self.lampMonitor
			self.lampMonitor.stopQuery = False
			if not self.lampMonitor.isAlive():
				self.lampMonitor.start()

	def showAlarmMonitor(self):
		if self.showing != self.alarmMonitor:
			self.stopCurrent()

			self.showing = self.alarmMonitor
			self.alarmMonitor.stopQuery = False
			if not self.alarmMonitor.isAlive():
				self.alarmMonitor.start()

	def showWaterMonitor(self):
		if self.showing != self.waterMonitor:
			self.stopCurrent()

			self.showing = self.waterMonitor
			self.waterMonitor.stopQuery = False
			if not self.waterMonitor.isAlive():
				self.waterMonitor.start()

	def line1(self):
		self.monitoring = tk.Label(self, text="Controle da Casa", bg="white",font=self.labelFont)
		self.monitoring.place(x=0, 
							  y=0,
							  width=self.screenWidth,
							  height=self.labelHeight)

	def line2(self):

		self.wmBtn = tk.Button( self, text = "Água", fg="blue", bg="white", 
								activebackground="white",font=self.btnFont,
								command=self.showWaterMonitor)
		self.wmBtn.place(x=self.distBetweenBtnSecLine,
						 y=self.labelHeight + self.distBetweenLines,
						 width=self.screenWidth*0.20,
						 height=self.screenHeight*0.05)

		self.amBtn = tk.Button( self, text = "Alarme", fg="red", bg="white", activebackground="white",font=self.btnFont,
								command=self.showAlarmMonitor)
		self.amBtn.place(x = self.screenWidth*0.20 + self.distBetweenBtnSecLine*2,
						 y = self.labelHeight + + self.distBetweenLines,
						 width= self.screenWidth*0.20,
						 height= self.screenHeight*0.05)

		self.imBtn = tk.Button( self, text = "Iluminação", fg="green", bg="white", activebackground="white",font=self.btnFont,
								command=self.showLampMonitor)
		self.imBtn.place(x = self.screenWidth*0.40 + self.distBetweenBtnSecLine*3,
						 y = self.labelHeight + + self.distBetweenLines,
						 width = self.screenWidth*0.20,
						 height = self.screenHeight*0.05)

		self.tmBtn = tk.Button( self, text = "Temperatura", fg="orange", bg="white", activebackground="white",font=self.btnFont,
								command=self.showTempMonitor )

		self.tmBtn.place(x = self.screenWidth*0.60 + self.distBetweenBtnSecLine*4,
						 y = self.labelHeight + self.distBetweenLines,
						 width = self.screenWidth*0.20,
						 height = self.screenHeight*0.05)			 

app = Main()
app.mainloop()