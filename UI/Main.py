from Tkinter import *
import tkFont as font
from ..Async.TemperatureMonitor import TemperatureMonitor 

class Main:

    def __init__( self, root ):
		self.screenWidth = root.winfo_screenwidth()-10
		self.screenHeight = root.winfo_screenheight()-10

		root.geometry(str(self.screenWidth)+"x"+str(self.screenHeight))
		root.wm_title("Controle da casa")
		root.configure(background="white")

		#distancia entre linhas.
		self.distBetweenLines = self.screenHeight*0.01

		#distancia entre botoes na segunda linha.
		self.distBetweenBtnSecLine = self.screenWidth*0.04

		#distancia entre botoes na quarta linha.
		self.distBetweenBtnFourthLine = self.screenWidth*0.1
		self.labelHeight = 0.10*self.screenHeight

		self.labelFont = font.Font(weight="normal",size=20)
		self.btnFont = font.Font(weight="normal",size=14)

		self.temMonitor = TemperatureMonitor()
		self.line1()
		self.line2()
		self.line3()
		self.line4()
		
    def line1(self):

		self.monitoring = Label(root, text="Monitoramento", bg="white",font=self.labelFont)
		self.monitoring.place(x=0, 
		                      y=0,
                              width=self.screenWidth,
                              height=self.labelHeight)

    def line2(self):

		self.wmBtn = Button( root, text = "Agua", fg="blue", bg="white", activebackground="white",font=self.btnFont)
		self.wmBtn.place(x=self.distBetweenBtnSecLine,
				         y=self.labelHeight + 5,
				         width=self.screenWidth*0.20,
				         height=self.screenHeight*0.10)

		self.amBtn = Button( root, text = "Alarme", fg="red", bg="white", activebackground="white",font=self.btnFont)
		self.amBtn.place(x = self.screenWidth*0.20 + self.distBetweenBtnSecLine*2,
        				 y = self.labelHeight + 5,
		        		 width= self.screenWidth*0.20,
		        		 height= self.screenHeight*0.10)

		self.imBtn = Button( root, text = "Iluminacao", fg="green", bg="white", activebackground="white",font=self.btnFont)
		self.imBtn.place(x = self.screenWidth*0.40 + self.distBetweenBtnSecLine*3,
		        		 y = self.labelHeight + 5,
		        		 width = self.screenWidth*0.20,
		        		 height = self.screenHeight*0.10)

		self.tmBtn = Button( root, text = "Temperatura", fg="orange", bg="white", activebackground="white",font=self.btnFont)
		self.tmBtn.place(x = self.screenWidth*0.60 + self.distBetweenBtnSecLine*4,
		        		 y = self.labelHeight + self.distBetweenLines,
					     width = self.screenWidth*0.20,
					     height = self.screenHeight*0.10)
		self.tmBtn.bind('<Button>', self.temMonitor.event )
					     
					
    def line3(self):

        self.commands = Label(root, text="Acionamentos", bg="white", activebackground="white", font = self.labelFont)
        self.commands.place(x = 0,
			                y = 2*(self.labelHeight + self.distBetweenLines),
			                width = self.screenWidth,
			                height = self.labelHeight)
					   
    def line4(self):

		self.waBtn = Button( root, text = "Agua", fg="blue", bg="white", activebackground="white",font=self.btnFont)
		self.waBtn.place(x = self.distBetweenBtnFourthLine,
				         y = 3*(self.labelHeight + self.distBetweenLines),
				         width = self.screenWidth*0.20,
				         height = self.screenHeight*0.10)

		self.aaBtn = Button( root, text = "Alarme", fg="red", bg="white", activebackground="white",font=self.btnFont)
		self.aaBtn.place(x = self.screenWidth*0.2 + self.distBetweenBtnFourthLine*2,
				         y = 3*(self.labelHeight + self.distBetweenLines),
				         width = self.screenWidth*0.20,
				         height = self.screenHeight*0.10)

		self.iaBtn = Button( root, text = "Iluminacao", fg="green", bg="white", activebackground="white",font=self.btnFont)
		self.iaBtn.place(x = self.screenWidth*0.4 + self.distBetweenBtnFourthLine*3,
				         y = 3*(self.labelHeight + self.distBetweenLines),
				         width = self.screenWidth*0.20,
				         height = self.screenHeight*0.10)

root = Tk()
app = Main(root)
root.mainloop()
