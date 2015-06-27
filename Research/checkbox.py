# Programa que instancia um objeto CheckBox e printa o estado do checkbox
# Recebe como parametro o texto e a funcao que executa quando clicado.


from Tkinter import *
from PIL import Image


class CheckBox:
	def __init__(self, txt, action):
		# var serve para pegar o status do checkbox
		self.var = IntVar()
		self.button = Checkbutton(master, text = txt, command = action, cursor = "hand2", variable = self.var)
			
	def Pack(self):
		self.button.pack()
	
	def Update(self):
		self.Pack()
		self.button.update()
	
	def getState(self):
		return self.var.get()
	
	
master = Tk()
b = CheckBox(txt = "clique", action = None)
while True:
	
	print b.getState()
		
	b.Update()
	
b.button.mainloop()


	
	





