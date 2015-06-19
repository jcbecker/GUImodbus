from Async.MyThread import MyThread
from Async.Monitor import Monitor
from Async.AlarmMonitor import AlarmMonitor
from Async.TemperatureMonitor import TemperatureMonitor
from Async.LampMonitor import LampMonitor
from Resources.Temperature import Temperature
from Resources.Lamp import Lamp
from Resources.Alarm import Alarm
import time

tm = TemperatureMonitor( "Temperature", Temperature() )
ta = AlarmMonitor( "Alarm", Alarm() )
lm = LampMonitor("Lamp", Lamp())
t = MyThread( [ tm, ta, lm ] )

t.start()
