import tkFont as font
import Tkinter as tk
import threading

from TemperatureMonitor import TemperatureMonitor 
from LampMonitor import LampMonitor

class Main(tk.Tk):

	def __init__( self ):
		tk.Tk.__init__(self)
		self.screenWidth = self.winfo_screenwidth()-10
		self.screenHeight = self.winfo_screenheight()-10

		self.geometry(str(self.screenWidth)+"x"+str(self.screenHeight))
		self.wm_title("Controle da casa")
		self.configure(background="white")

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
		self.line3()
		self.line4()

		self.actions = tk.Frame(height = self.screenHeight*0.63,width=self.screenWidth,bg="white")
		self.actions.pack(side="bottom", fill="x", expand = False)
		self.actions.grid_rowconfigure(0,weight=1)		
		self.actions.grid_columnconfigure(0,weight=1)

		self.showing = None
		self.tempMonitor = TemperatureMonitor(self.actions,self)
		self.lampMonitor = LampMonitor(self.actions,self)

	def showTempMonitor(self):
		if self.showing is not None:
			self.showing.stopQuery = True

		self.showing = self.tempMonitor
		self.showing.stopQuery = False
		if not self.tempMonitor.isAlive():
			self.tempMonitor.start()
		self.tempMonitor.tkraise()

	def showLampMonitor(self):

		if self.showing is not None:
			self.showing.stopQuery = True

		self.showing = self.lampMonitor
		self.lampMonitor.stopQuery = False
		if not self.lampMonitor.isAlive():
			self.lampMonitor.start()
		self.lampMonitor.tkraise()

	def line1(self):
		self.monitoring = tk.Label(self, text="Monitoramento", bg="white",font=self.labelFont)
		self.monitoring.place(x=0, 
							  y=0,
							  width=self.screenWidth,
							  height=self.labelHeight)

	def line2(self):

		self.wmBtn = tk.Button( self, text = "Agua", fg="blue", bg="white", activebackground="white",font=self.btnFont)
		self.wmBtn.place(x=self.distBetweenBtnSecLine,
						 y=self.labelHeight + self.distBetweenLines,
						 width=self.screenWidth*0.20,
						 height=self.screenHeight*0.05)

		self.amBtn = tk.Button( self, text = "Alarme", fg="red", bg="white", activebackground="white",font=self.btnFont)
		self.amBtn.place(x = self.screenWidth*0.20 + self.distBetweenBtnSecLine*2,
						 y = self.labelHeight + + self.distBetweenLines,
						 width= self.screenWidth*0.20,
						 height= self.screenHeight*0.05)

		self.imBtn = tk.Button( self, text = "Iluminacao", fg="green", bg="white", activebackground="white",font=self.btnFont,
								command=lambda:self.showLampMonitor())
		self.imBtn.place(x = self.screenWidth*0.40 + self.distBetweenBtnSecLine*3,
						 y = self.labelHeight + + self.distBetweenLines,
						 width = self.screenWidth*0.20,
						 height = self.screenHeight*0.05)

		self.tmBtn = tk.Button( self, text = "Temperatura", fg="orange", bg="white", activebackground="white",font=self.btnFont,
								command=lambda:self.showTempMonitor() )

		self.tmBtn.place(x = self.screenWidth*0.60 + self.distBetweenBtnSecLine*4,
						 y = self.labelHeight + self.distBetweenLines,
						 width = self.screenWidth*0.20,
						 height = self.screenHeight*0.05)
						 
					
	def line3(self):

		self.commands = tk.Label(self, text="Acionamentos", bg="white", activebackground="white", font = self.labelFont)
		self.commands.place(x = 0,
							y = 2*(self.labelHeight + self.distBetweenLines),
							width = self.screenWidth,
							height = self.labelHeight)
					   
	def line4(self):

		self.waBtn = tk.Button( self, text = "Agua", fg="blue", bg="white", activebackground="white",font=self.btnFont)
		self.waBtn.place(x = self.distBetweenBtnFourthLine,
						 y = 3*(self.labelHeight + self.distBetweenLines),
						 width = self.screenWidth*0.20,
						 height = self.screenHeight*0.05)

		self.aaBtn = tk.Button( self, text = "Alarme", fg="red", bg="white", activebackground="white",font=self.btnFont)
		self.aaBtn.place(x = self.screenWidth*0.2 + self.distBetweenBtnFourthLine*2,
						 y = 3*(self.labelHeight + self.distBetweenLines),
						 width = self.screenWidth*0.20,
						 height = self.screenHeight*0.05)

		self.iaBtn = tk.Button( self, text = "Iluminacao", fg="green", bg="white", activebackground="white",font=self.btnFont)
		self.iaBtn.place(x = self.screenWidth*0.4 + self.distBetweenBtnFourthLine*3,
						 y = 3*(self.labelHeight + self.distBetweenLines),
						 width = self.screenWidth*0.20,
						 height = self.screenHeight*0.05)

app = Main()
app.mainloop()