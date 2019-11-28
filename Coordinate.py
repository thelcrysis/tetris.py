class Coordinate:
	x = 0
	y = 0
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def setCoordinate(self,x,y):
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