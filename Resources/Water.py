#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from ..IO.ModBusReader import ModBusReader
from ..IO.ModBusWriter import ModBusWriter

class Water:

	def __init__(self):	
		self.reg = {}	
		self.reader = ModBusReader()
		self.writer = ModBusWriter()

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
		
		
	def HotBathtub (self):
		comReg = "0008"
		regNumber = "0001"
		
		answer = self.reader.read(comReg, regNumber)
		if answer [5:7] != "02":
			raise IOError ("HotWaterBathtub AnswerException")
		
		regState = (int(answer[7:11],16))
		
		if (regState & 2)== 0:
			regData = regState | 2
		else:
			regData = ~ 2
			regData = regData & regState 
		
		regData = hex(regData)[2:]
		
		l = len(regData)
		
		while l < 4 :
			regData="0"+regData
			l=len(regData)
		
		status = self.writer.write (comReg,regData)
		
		if not status:
			raise IOError("HotWaterBathtub WriteException") 
		return status

	def ColdBathtub (self):
		comReg = "0008"
		regNumber = "0001"
		
		answer = self.reader.read(comReg, regNumber)
		if answer [5:7] != "02":
			raise IOError ("ColdWaterBathtub AnswerException")
		
		regState = (int(answer[7:11],16))
		
		if (regState & 4)== 0:
			regData = regState | 4
		else:
			regData = ~ 4
			regData = regData & regState 
		
		regData = hex(regData)[2:]
		
		l = len(regData)
		
		while l < 4 :
			regData="0"+regData
			l=len(regData)
		
		status = self.writer.write (comReg,regData)
		
		if not status:
			raise IOError("ColdWaterBathtub WriteException") 
		return status
	
	
	def ExhaustBathtub (self):
		comReg = "0008"
		regNumber = "0001"
		
		answer = self.reader.read(comReg, regNumber)
		if answer [5:7] != "02":
			raise IOError ("ExhaustBathtub AnswerException")
		
		regState = (int(answer[7:11],16))
		
		if (regState & 8)== 0:
			regData = regState | 8
		else:
			regData = ~ 8
			regData = regData & regState 
		
		regData = hex(regData)[2:]
		
		l = len(regData)
		
		while l < 4 :
			regData="0"+regData
			l=len(regData)
		
		status = self.writer.write (comReg,regData)
		
		if not status:
			raise IOError("ExhaustBathtub WriteException") 
		return status
	
	
	def HotPool (self):
		comReg = "0008"
		regNumber = "0001"
		
		answer = self.reader.read(comReg, regNumber)
		if answer [5:7] != "02":
			raise IOError ("HotPool AnswerException")
		
		regState = (int(answer[7:11],16))
		
		if (regState & 16)== 0:
			regData = regState | 16
		else:
			regData = ~ 16
			regData = regData & regState 
		
		regData = hex(regData)[2:]
		
		l = len(regData)
		
		while l < 4 :
			regData="0"+regData
			l=len(regData)
		
		status = self.writer.write (comReg,regData)
		
		if not status:
			raise IOError("HotPool WriteException") 
		return status
	
	
	
	def ColdPool (self):
		comReg = "0008"
		regNumber = "0001"
		
		answer = self.reader.read(comReg, regNumber)
		if answer [5:7] != "02":
			raise IOError ("ColdPool AnswerException")
		
		regState = (int(answer[7:11],16))
		
		if (regState & 32)== 0:
			regData = regState | 32
		else:
			regData = ~ 32
			regData = regData & regState 
		
		regData = hex(regData)[2:]
		
		l = len(regData)
		
		while l < 4 :
			regData="0"+regData
			l=len(regData)
		
		status = self.writer.write (comReg,regData)
		
		if not status:
			raise IOError("ColdPool WriteException") 
		return status
