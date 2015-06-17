from Resources.Water import Water
from Resources.Alarm import Alarm
from IO.ModBusWriter import ModBusWriter
from IO.ModBusReader import ModBusReader
import time

alarm = Alarm()

alarm.fired()
#monitReg = "000A"

time.sleep(2)

mw = ModBusWriter()
mw.write("0001", "0001" )

alarm.fired()
#mbw
