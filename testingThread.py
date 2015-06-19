from Async.MyThread import MyThread
from Async.Monitor import Monitor
from Resources.Temperature import Temperature
from Resources.Lamp import Lamp

t = MyThread("Temperature", Monitor( "Temperature", Temperature() ) )
t2 = MyThread("Lamp", Monitor( "Lamp", Lamp() ) )

t.start()
t2.start()