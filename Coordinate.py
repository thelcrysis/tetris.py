class Coordinate:
	x = 0
	y = 0
	def __init__(self,x=0,y=0):
		self.x = x
		self.y = y

	def setCoordinate(self,x=0,y=0):
		self.x = x
		self.y = y
	def drop(self):
		self.y += 1
	def left(self):
		self.x -= 1
	def right(self):
		self.x += 1
	def __str__(self):
		outputString = '('+str(self.x)+','+str(self.y)+')'
		return outputString
	def getX(self): return self.x
	def getY(self): return self.y