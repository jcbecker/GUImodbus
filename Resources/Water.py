from ..IO.ModBusReader import ModBusReader
from ..IO.ModBusWriter import ModBusWriter

class Water:

	comReg7 = {}
	comReg9 = {}

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
			
		print answer
		
		waters = []
		waters.append(int(answer[7:11], 16))
		waterState = (int(answer[15:19], 16))
		
		if (waterState & 4) == 0 :
			waters.append(0)
		else:
			waters.append(1)
		
		if (waterState & 8) == 0:
			waters.append(0)
		else:
			waters.append(1)
		
		if (waterState & 16) == 0:
			waters.append(0)
		else:
			waters.append(1)
		
		if (waterState & 32) == 0:
			waters.append(0)
		else:
			waters.append(1)
		
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
		
		
	def comOnOfHotWater(self):
		comReg = "0008"
		regNumber = "0001"
		
		answer = self.reader.read(comReg, regNumber)
		
		if answer[5]+answer[6] != "02":
			raise IOError("WaterAnswerException")
		
		
		waters = []
		waterState = (int(answer[7:11], 16))
		
		
		
		
		
		if (waterState & 2) == 0 :
			waters.append(0)
		else:
			waters.append(1)
		
		if (waterState & 4) == 0:
			waters.append(0)
		else:
			waters.append(1)
		
		if (waterState & 8) == 0:
			waters.append(0)
		else:
			waters.append(1)
		
		if (waterState & 16) == 0:
			waters.append(0)
		else:
			waters.append(1)
		
		if (waterState & 32) == 0:
			waters.append(0)
		else:
			waters.append(1)
		
		
		
