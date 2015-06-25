#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from ..IO.ModBusWriter import ModBusWriter
from ..IO.ModBusReader import ModBusReader

import time

class Alarm:

	def __init__(self):		
		self.writer = ModBusWriter()
		self.reader = ModBusReader()

		answer = self.reader.read("0008","0001")
		self.regState = int( answer[7:11], 16 )

	#usa o bit 0 do registrador 8 para
	#ligar ou desligar o alarme da casa
	#retorna false se o alarme foi desligado
	#retorna true se o alarme foi ligado.
	def ONOFF( self ):
		comReg = "0008"
		regNumber = "0001"

		regData = self.regState
		if regData & 1:
			regData = regData - 1
			self.state = False
		else:
			self.state = True
			regData = regData + 1

		copy = regData
		regData = hex(regData)[2:]

		l = len(regData)

		if l == 1:
			regData = "000"+regData
		elif l == 2:
			regData = "00"+regData
		elif l == 3:
			regData = "0"+regData

		if self.writer.write( comReg, regData.upper() ):
			self.regState = copy
			return self.state
		
		raise IOError("AlarmAnswerException")

	def readAnswer(self):
		monitReg = "0009"
		regNumber = "0002"

		self.answer = self.reader.read( monitReg, regNumber )

		if self.answer[5]+self.answer[6] != "04":
			raise IOError("AlarmAnswerException")	
	

	#fazer todas as buscas de uma vez só.
	def alarmInf( self ):
		self.readAnswer()

		inf = []
		reg9Data = int( self.answer[7:11], 16 )

		inf.append((reg9Data & 1) != 0)
		inf.append((reg9Data & 2) != 0)
		inf.append(int( self.answer[11:15], 16 ))

		return inf