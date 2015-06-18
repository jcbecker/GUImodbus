from Resources.Water import Water
from Resources.Alarm import Alarm
from IO.ModBusWriter import ModBusWriter
from IO.ModBusReader import ModBusReader
import time

mw = ModBusWriter()
print "Resposta da escrita: " +mw.write("0009", "0001" )

a = Alarm()
if a.fired():
	print "O alarme esta disparado"
else:
	print "O alarme nao esta disparado"

print "Resposta da escrita: " +mw.write("0009", "0002" )

a = Alarm()
if a.fired():
	print "O alarme esta disparado"
else:
	print "O alarme nao esta disparado"

#mbw
