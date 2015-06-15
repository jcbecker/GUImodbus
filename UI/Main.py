from Tkinter import *

root = Tk()
screenWidth = root.winfo_screenwidth()-10
screenHeight = root.winfo_screenheight()-10

root.geometry(str(screenWidth)+"x"+str(screenHeight))
root.wm_title("Controle da casa")
root.configure(background="white")

distBetweenLines = screenHeight*0.01
distBetweenBtnSecLine = screenWidth*0.04
distBetweenBtnFourthLine = screenWidth*0.1
labelHeight = 0.10*screenHeight

monitoring = Label(root, text="Monitoramento", bg="white")
monitoring.place(x=0,y=0,width=screenWidth,height=labelHeight)

wmBtn = Button( root, text = "Água", fg="blue", bg="white")
wmBtn.place(x=distBetweenBtnSecLine,
			y=labelHeight + 5,
			width=screenWidth*0.20,
			height=screenHeight*0.10)

amBtn = Button( root, text = "Alarme", fg="red", bg="white")
amBtn.place(x = screenWidth*0.20 + distBetweenBtnSecLine*2,
			y = labelHeight + 5,
			width= screenWidth*0.20,
			height= screenHeight*0.10)

imBtn = Button( root, text = "Iluminação", fg="green", bg="white")
imBtn.place(x = screenWidth*0.40 + distBetweenBtnSecLine*3,
		    y = labelHeight + 5,
		    width = screenWidth*0.20,
		    height = screenHeight*0.10)

tmBtn = Button( root, text = "Temperatura", fg="orange", bg="white")
tmBtn.place(x = screenWidth*0.60 + distBetweenBtnSecLine*4,
			y = labelHeight + distBetweenLines,
			width = screenWidth*0.20,
			height = screenHeight*0.10)

commands = Label(root, text="Acionamentos", bg="white")
commands.place(x = 0,
			   y = 2*(labelHeight + distBetweenLines),
			   width = screenWidth,
			   height = labelHeight)

waBtn = Button( root, text = "Água", fg="blue", bg="white")
waBtn.place(x = distBetweenBtnFourthLine,
		    y = 3*(labelHeight + distBetweenLines),
		    width = screenWidth*0.20,
		    height = screenWidth*0.10)

aaBtn = Button( root, text = "Alarme", fg="red", bg="white")
aaBtn.place(x = screenWidth*0.2 + distBetweenBtnFourthLine*2,
		    y = 3*(labelHeight + distBetweenLines),
		    width = screenWidth*0.20,
		    height = screenWidth*0.10)

iaBtn = Button( root, text = "Iluminação", fg="green", bg="white")
iaBtn.place(x = screenWidth*0.4 + distBetweenBtnFourthLine*3,
		    y = 3*(labelHeight + distBetweenLines),
		    width = screenWidth*0.20,
		    height = screenWidth*0.10)

root.mainloop()