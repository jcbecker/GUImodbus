from Async.MyThread import MyThread
from Async.Monitor import Monitor
from Async.AlarmMonitor import AlarmMonitor
from Resources.Temperature import Temperature
from Resources.Lamp import Lamp
from Resources.Alarm import Alarm

t = MyThread( Monitor( "Temperature", Temperature() ) )

alarm = AlarmMonitor( "Alarm", Alarm() )
t2 = MyThread( alarm )

t.start()
t2.start()