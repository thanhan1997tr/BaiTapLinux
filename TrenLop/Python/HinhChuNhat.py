class HinhChuNhat:
	def __init__(self, Ten, Dai, Rong):
		self.Ten = Ten
		self.Dai = Dai
		self.Rong = Rong
	def getTen(self):
		return self.Ten
	def getDai(self):
		return self.Dai
	def getRong(self):
		return self.Rong
	def getCV(self):
		return (self.Dai + self.Rong)*2
	def getDT(self):
		return self.Dai * self.Rong
	def toString(self):
		print "%s(%d,%d)" % (self.Ten, self.Dai,self.Rong)
		return 0