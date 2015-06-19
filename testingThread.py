from Async.MyThread import MyThread
from Async.Monitor import Monitor
from Async.AlarmMonitor import AlarmMonitor
from Async.TemperatureMonitor import TemperatureMonitor
from Resources.Temperature import Temperature
from Resources.Lamp import Lamp
from Resources.Alarm import Alarm
import time

tm = TemperatureMonitor( "Temperature", Temperature() )
t = MyThread( tm )

ta = AlarmMonitor( "Alarm", Alarm() )
t2 = MyThread( ta )

t.start()
time.sleep(2)
t2.start()
