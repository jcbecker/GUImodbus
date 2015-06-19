from Resources.Water import Water
from Resources.Alarm import Alarm
from Resources.Lamp import Lamp
from Resources.Temperature import Temperature
from IO.ModBusWriter import ModBusWriter
from IO.ModBusReader import ModBusReader
import time

water = Water()
mv = ModBusWriter()
reader =  ModBusReader()

for i in range(12):

	print "digite oq vc quer mudar opcoes"
	print "hotbathtub       = hb"
	print "coldbathtub      = cb"
	print "ExhaustBathtub   = eb"
	print "hotpool          = hp"
	print "coldpool         = cp"
	stdin = raw_input ()

	if stdin == "hb":
		water.HotBathtub()
		
	elif stdin == "cb":
		water.ColdBathtub()
		
	elif stdin == "eb":
		water.ExhaustBathtub()
		
	elif stdin == "hp":
		water.HotPool()
		
	elif stdin == "cp":
		water.ColdPool()
		
	else:
		print "nada foi escolhido"

	answer = reader.read("0008", "0001")
	retState = (int(answer[7:11],16))



	if (retState & 2)== 0:
		print "hotbathtub off"
	else:
		print "hotbathtub on"

	if (retState & 4)== 0:
		print "coldbathtub off"
	else:
		print "coldbathtub on"

	if (retState & 8)== 0:
		print "ExhaustBathtub off"
	else:
		print "ExhaustBathtub on"
		
	if (retState & 16)== 0:
		print "HotPool off"
	else:
		print "HotPool on"

	if (retState & 32)== 0:
		print "ColdPool off"
	else:
		print "ColdPool on"



#for i in range(12):
#	if water.HotBathtub():
#		print "ok"
#	answer = reader.read("0008", "0001")
#	print answer





"""
if mv.write("0007","0008"):
	print "escreveu no registrador 7, registrador do nivel da agua"

if mv.write ("0009","0000"):
	print "escreveu no registrador 9, ligou o bit 4, terceiro"



for i in water.MonitWater():
	print i

aqui acaba uma e começa outro teste 


lamp = Lamp()
if lamp.comLamp1("0002"):
	print "Conseguiu escrever"
	
print lamp.monitLamps()[0]

mw = ModBusWriter()
if mw.write("000B", "0020"):
	print "escreveu no registrador 11"
	
if mw.write("000C", "0080"):
	print "escreveu no registrador 12"
	
if mw.write("000D", "0010"):
	print "escreveu no registrador 13"

lamp.monitLamps()	
#--inicio do teste da verificacao do alarme em todos os locais.
#a = Alarm()
#if a.checkAlarm("garagem"):
#	print "O alarme da garagem esta ligado."
#else:
#	print "O alarme da garagem esta desligado."

#mw = ModBusWriter()
#if mw.write("000A","0002"):
#	print "O alarme da piscina foi aceso."

#if a.checkAlarm("piscina1"):
#	print "O alarme da piscina esta ligado."
#else:
#	print "O alarme da piscina esta desligado."

#if a.checkAlarm("cozinha"):
#	print "O alarme da cozinha esta ligado."
#else:
#	print "O alarme da cozinha esta desligado."
#--fim do teste da verificacao do alarme em todos os locais.

#--inicio do teste da ligacao do alarme e da checagem
#para verificar se o alarme esta ligado ou nao
#a = Alarm()

#if a.checkONOFF():
#	print "O alarme agora esta ligado."
#else:
#	print "O alarme agora esta desligado."

#	if a.ONOFF():
#		print "Agora o alarme foi ligado."
#--fim do teste da ligacao do alarme e da checagem

#--inicio do teste do disparo do alarme
#mw = ModBusWriter()
#if mw.write("0009", "0000" ):
	#print "Os dados foram escritos." 
#else:
	#print "Os dados nao foram escritos."

#a = Alarm()
#if a.fired():
#	print "O alarme esta disparado"
#else:
#	print "O alarme nao esta disparado"

#if mw.write("0009", "0002" ):
#	print "Os dados foram escritos." 
#else:
#	print "Os dados nao foram escritos."

#if a.fired():
#	print "O alarme esta disparado"
#else:
#	print "O alarme nao esta disparado"
#--fim do teste do disparo do alarme
#mbw
"""
