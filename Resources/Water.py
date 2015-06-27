#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from ..IO.ModBusReader import ModBusReader
from ..IO.ModBusWriter import ModBusWriter

class Water:

	def __init__(self,alarm):	
		self.reader = ModBusReader()
		self.writer = ModBusWriter()

		answer = self.reader.read("0008","0001")
		self.alarmRegState = alarm

	def MonitWater(self):
		monitReg = "0007"
		regNumber = "0003"
		
		answer = self.reader.read(monitReg,regNumber)
		
		if answer[5:7] != "06":
			raise IOError ("Wrong answer exception")
			
		#print answer
		
		waters = []
		waters.append(int(answer[7:11], 16))
		
		waterState = (int(answer[15:19], 16))
		for i in range(2,6):
			waters.append( (waterState & (1 << i)) != 0 )
				
		return waters
		
	def tap(self, pw ):
		comReg = "0008"
		
		pw = ( 1 << pw )

		if (self.alarmRegState.regState & pw ) == 0:
			status = True
			regData = self.alarmRegState.regState | pw
		else:
			status = False
			regData = ~ pw
			regData = regData & self.alarmRegState.regState 
		
		copy = regData
		regData = hex(regData)[2:]
		
		l = len(regData)
		
		while l < 4 :
			l = l + 1
			regData="0"+regData

		if not self.writer.write (comReg,regData.upper()):
			raise IOError("WriteException") 
		
		self.alarmRegState.regState = copy
		#tem que retornar se ta ligada ou
		#desligada. E não se conseguiu escrever,
		#se conseguiu escrever ou não quem retorna
		#é a exceção.	
		return status
