from Resources.Water import Water
from Resources.Alarm import Alarm
from IO.ModBusWriter import ModBusWriter
from IO.ModBusReader import ModBusReader

alarm = Alarm()

alarm.fired()
#monitReg = "000A"

mw = ModBusWriter()
mw.write("0009",0, "0001" )
alarm.fired()
#mbw
