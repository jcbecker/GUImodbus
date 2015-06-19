from Tkinter import *
import time

import threading
import time

class testingMonitor(threading.Thread):

    def __init__(self):
        pass
        
    def evento(self, w):
				              
        self.run()
        
    def fechar(self):
        threading.Event().set()
				                    
    def run(self):
        self.tempView = Tk()
        self.tempView.geometry("300x300")   
        self.tempView.protocol("WM_DELETE_WINDOW", self.fechar() )
        self.monitoring = Label(self.tempView, text="Monitoramento", bg="white") 
        self.monitoring.place(x=0,
				              y=0,
				              width=150,
				              height=150)
				    
        k = 0
        while True:
            #atualizar.
            self.monitoring.config(text=str(k))
            self.tempView.update()
            k = k + 1
            time.sleep(1)
            
            if k == 10:
                break
        
