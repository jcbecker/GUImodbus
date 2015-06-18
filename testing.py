from Resources.Water import Water
from Resources.Alarm import Alarm
from IO.ModBusWriter import ModBusWriter
from IO.ModBusReader import ModBusReader
import time

a = Alarm()
print "Leitura: " + a.fired()
mw = ModBusWriter()
mw.write("0009", "0001" )

mr = ModBusReader()
print "Resposta da escrita: " + mr.receive() 

#mbw
