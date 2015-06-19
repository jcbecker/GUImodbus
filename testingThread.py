from Async.MyThread import MyThread
from Async.Controller import Controller
from Resources.Temperature import Temperature
from Resources.Lamp import Lamp

t = MyThread("Temperature", Controller( "Temperature", Temperature() ) )
t2 = MyThread("Lamp", Controller( "Lamp", Lamp() ) )

t.start()
t2.start()