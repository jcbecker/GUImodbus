#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from ..IO.ModBusReader import ModBusReader
from ..IO.ModBusWriter import ModBusWriter

class Lamp:

	def __init__(self):
		self.reader = ModBusReader()
		self.writer = ModBusWriter()

	def monitLamps(self):
		monitReg = "000B"
		regNumber = "0003"
		
		answer = self.reader.read(monitReg,regNumber)
		
		if answer[5:7] != "06":
			raise IOError ("Wrong answer exception")
		
		lamps = []
		lamps.append( int( answer[7:11], 16 ) )
		lamps.append( int( answer[11:15], 16 ) )
		lamps.append( int( answer[15:19], 16 ) )
		
		return lamps


	def LampWrite(self, Reg, data):
		if not self.writer.write(Reg, data):
			if not self.writer.write(Reg, data):
				raise Exception("WriteException")
		else:
			return True

	#implementar direito os métodos de leitura
	#e de escrita.
	def comLamp1(self,data):
		Reg = "000E"
		return self.LampWrite(Reg, data)

	def comLamp2(self,data):
		Reg = "000F"
		return self.LampWrite(Reg, data)

	def comLamp3(self,data):
		Reg = "0010"
		return self.LampWrite(Reg, data)
			
			
	
