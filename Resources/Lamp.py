#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from ..IO.ModBusReader import ModBusReader
from ..IO.ModBusWriter import ModBusWriter

class Lamp:

	reg = []

	def __init__(self):
		self.reader = ModBusReader()
		self.writer = ModBusWriter()

		#monitoradores.
		answer = self.reader.read("000E","0003")
		self.reg.append( int(answer[7:11],16) )
		self.reg.append( int(answer[11:15],16) )
		self.reg.append( int(answer[15:19],16) )
		
	def initSlave(self):
		self.hexModBus("000E",0)
		self.hexModBus("000F",1)
		self.hexModBus("0010",2)
	
	def hexModBus(self, redID, i ):
	
		regData = hex(self.reg[i])[2:]

		l = len(regData)

		while l < 4:
			regData = "0"+regData
			l = l + 1
			
		try:
			self.writer.write(redID, regData.upper() )
			return True
		except Exception as e:
			return False		

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

	def switch(self,regID,pw):

		regIdx = int( regID, 16 ) - 14
		
		pw = ( 1 << pw )
		if ( self.reg[regIdx] & pw ) == 0:
			status = True
			regData = self.reg[regIdx] | pw
		else:
			status = False
			regData = ~ pw
			regData = regData & self.reg[regIdx]

		copy = regData
		regData = hex(regData)[2:]

		l = len(regData)

		while l < 4:
			l = l + 1
			regData = "0"+regData

		if not self.writer.write(regID,regData.upper()):
			raise IOError("WriteException")

		self.reg[regIdx] = copy

		return status
