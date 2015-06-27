#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from ..IO.ModBusWriter import ModBusWriter
from TemperatureMonitor import TemperatureMonitor 
from WaterMonitor import WaterMonitor
from AlarmMonitor import AlarmMonitor
from LampMonitor import LampMonitor

from tkMessageBox import *
import tkFont as font
import Tkinter as tk
import ttk
import threading
import time
import tkFileDialog

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
		self.toolBar()
		self.tempMonitor = TemperatureMonitor(self.actions,self)
		self.alarmMonitor = AlarmMonitor(self.actions,self)
		self.waterMonitor = WaterMonitor(self.actions,self,self.alarmMonitor.user)
		self.lampMonitor = LampMonitor(self.actions,self)


	def	 toolBar(self):
		self.menuBar = tk.Menu(self)
		
		self.config(menu=self.menuBar)
		
		self.menuBar.add_command(label="Salvar", command=self.save )
		self.menuBar.add_command(label="Carregar", command=self.load )
		self.menuBar.add_command(label="Instruções", command=self.instruction )
		self.menuBar.add_command(label="Fechar", command=self.quit )
		
	def save(self):
		state = "8="+str(self.alarmMonitor.user.regState)+"\n"
		state = state+"14="+str(self.lampMonitor.user.reg[0])+"\n"
		state = state+"15="+str(self.lampMonitor.user.reg[1])+"\n"
		state = state+"16="+str(self.lampMonitor.user.reg[2])
		
													#C:\\
		wFile = tkFileDialog.asksaveasfile(mode='w', initialdir = "/home/", title="Escolha o arquivo",
											filetypes=[("all files","*.mmj")] )
		
		wFile.write(state)
		
		wFile.close()
		
	def load(self):
		rFile = tkFileDialog.askopenfile(mode='r',initialdir = "/home/", title="Escolha o arquivo",
											filetypes=[("all files","*.mmj")])
			
		lines = rFile.read().split("\n")
		self.alarmMonitor.user.regState = int(lines[0].split("=")[1]) 
		self.alarmMonitor.user.initSlave()
		
		self.lampMonitor.user.reg[0] = int(lines[0].split("=")[1]) 
		self.lampMonitor.user.reg[1] = int(lines[1].split("=")[1])
		self.lampMonitor.user.reg[2] = int(lines[2].split("=")[1])
		self.lampMonitor.user.initSlave()

	def instruction(self):
		showinfo("Instruções", "Clique nas tabelas na área da água ou na área da Iluminação para abrir / fechar uma torneira ou ligar / desligar uma lâmpada. \nSe algum erro ocorrer durante a execução do comando uma linha vermelha aparecerá abaixo da tabela que foi utilizada. Aguarde alguns instantes e tente realizar o comando novamente, se a linha sumir o comando foi executado com sucesso. \n\nObs: A área do alarme e da temperatura não possui as funcionalidades citadas acima.")

	def quit(self):
		self.alarmMonitor.exit = True
		self.waterMonitor.exit = True
		self.tempMonitor.exit = True
		self.lampMonitor.exit = True
		
		self.alarmMonitor.stopQuery = True
		self.waterMonitor.stopQuery = True
		self.tempMonitor.stopQuery = True
		self.lampMonitor.stopQuery = True
		
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
