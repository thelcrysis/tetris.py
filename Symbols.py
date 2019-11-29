from Coordinate import *
class Symbols:
	center = Coordinate()
	leftCorner = Coordinate()
	symbolType = ''
	symbolFamily = ''
	def getSymbolType(self):
		return self.symbolType
	
	def getCenter(self):
		return self.center
	def nameToSymbol(self,name):
		if name == 'four': return self.four(self.leftCorner.getX(),self.leftCorner.getY())
		elif name == 'four90': return self.four90(self.leftCorner.getX(),self.leftCorner.getY())
		elif name == 'L': return self.L(self.leftCorner.getX(),self.leftCorner.getY())
		elif name == 'L90': return self.L90(self.leftCorner.getX(),self.leftCorner.getY())
		elif name == 'L180': return self.L180(self.leftCorner.getX(),self.leftCorner.getY())
		elif name == 'L270': return self.L270(self.leftCorner.getX(),self.leftCorner.getY())
		elif name == 'revL': return self.revL(self.leftCorner.getX(),self.leftCorner.getY())
		elif name == 'revL90': return self.revL90(self.leftCorner.getX(),self.leftCorner.getY())
		elif name == 'revL180': return self.revL180(self.leftCorner.getX(),self.leftCorner.getY())
		elif name == 'revL270': return self.revL270(self.leftCorner.getX(),self.leftCorner.getY())
		elif name == 'penis': return self.penis(self.leftCorner.getX(),self.leftCorner.getY())
		elif name == 'penis90': return self.penis90(self.leftCorner.getX(),self.leftCorner.getY())
		elif name == 'penis180': return self.penis180(self.leftCorner.getX(),self.leftCorner.getY())
		elif name == 'penis270': return self.penis270(self.leftCorner.getX(),self.leftCorner.getY())
		elif name == 'cube': return self.cube(self.leftCorner.getX(),self.leftCorner.getY())

	def four(self,x=0,y=0):
		self.center.setCoordinate(1,1)
		self.leftCorner.setCoordinate(x,y)
		self.symbolType = 'four'
		self.symbolFamily = 'Four'
		return [[".",".",".","."],
				['O','O','O','O'],
				[".",".",".","."],
				[".",".",".","."]]

	def four90(self,x=0,y=0):
		self.center.setCoordinate(1,1)
		self.leftCorner.setCoordinate(x,y)
		self.symbolType = 'four'
		self.symbolFamily = 'Four'
		return [[".","O",".","."],
				['.','O','.','.'],
				[".","O",".","."],
				[".","O",".","."]]

	def L(self,x=0,y=0):
		self.center.setCoordinate(1,1)		
		self.leftCorner.setCoordinate(x,y)
		self.symbolType = 'L'
		self.symbolFamily = 'L'

		return [['O','.','.','.'],
				["O","O","O","."],
				[".",".",".","."],
				[".",".",".","."]]

	def L90(self,x=0,y=0):
		self.center.setCoordinate(1,1)
		self.leftCorner.setCoordinate(x,y)
		self.symbolType = 'L90'
		self.symbolFamily = 'L'
		return [['.','O','O','.'],
				[".","O",".","."],
				[".","O",".","."],
				[".",".",".","."]]
	def L180(self,x=0,y=0):
		self.center.setCoordinate(1,1)
		self.leftCorner.setCoordinate(x,y)
		self.symbolType = 'L180'
		self.symbolFamily = 'L'
		return [['.','.','.','.'],
				["O","O","O","."],
				[".",".","O","."],
				[".",".",".","."]]
	def L270(self,x=0,y=0):
		self.center.setCoordinate(1,1)
		self.leftCorner.setCoordinate(x,y)
		self.symbolType = 'L270'
		self.symbolFamily = 'L'
		return [['.','O','.','.'],
				[".","O",".","."],
				["O","O",".","."],
				[".",".",".","."]]
		
	def revL(self,x=0,y=0):
		self.center.setCoordinate(1,1)
		self.leftCorner.setCoordinate(x,y)
		self.symbolType = 'revL'
		self.symbolFamily = 'RevL'
		
		return [['.','.','O','.'],
				["O","O","O","."],
				[".",".",".","."],
				[".",".",".","."]]

	def revL90(self,x=0,y=0):
		self.center.setCoordinate(1,1)
		self.leftCorner.setCoordinate(x,y)
		self.symbolType = 'revL180'
		self.symbolFamily = 'RevL'
		return [['.','O','.','.'],
				[".","O",".","."],
				[".","O","O","."],
				[".",".",".","."]]
	def revL180(self,x=0,y=0):
		self.center.setCoordinate(1,1)
		self.leftCorner.setCoordinate(x,y)
		self.symbolType = 'revL180'
		self.symbolFamily = 'RevL'
		return [['.','.','.','.'],
				["O","O","O","."],
				["O",".",".","."],
				[".",".",".","."]]
	def revL270(self,x=0,y=0):
		self.center.setCoordinate(1,1)
		self.leftCorner.setCoordinate(x,y)
		self.symbolType = 'revL270'
		self.symbolFamily = 'RevL'
		return [['O','O','.','.'],
				[".","O",".","."],
				[".","O",".","."],
				[".",".",".","."]]
	def cube(self,x=0,y=0):
		self.center.setCoordinate(1,1)
		self.leftCorner.setCoordinate(x,y)
		self.symbolType = 'cube'
		self.symbolFamily = 'Cube'
		
		return [['O','O','.','.'],
				["O","O",".","."],
				[".",".",".","."],
				[".",".",".","."]]

	def penis(self,x=0,y=0):
		self.center.setCoordinate(1,1)
		self.leftCorner.setCoordinate(x,y)
		self.symbolType = 'penis'
		self.symbolFamily = 'Penis'

		return [['.','O','.','.'],
				["O","O","O","."],
				[".",".",".","."],
				[".",".",".","."]]
	def penis90(self,x=0,y=0):
		self.center.setCoordinate(1,1)
		self.leftCorner.setCoordinate(x,y)
		self.symbolType = 'penis90'
		self.symbolFamily = 'Penis'
		return [['.','O','.','.'],
				[".","O","O","."],
				[".","O",".","."],
				[".",".",".","."]]
	def penis180(self,x=0,y=0):
		self.center.setCoordinate(1,1)
		self.leftCorner.setCoordinate(x,y)
		self.symbolType = 'penis180'
		self.symbolFamily = 'Penis'
		return [['.','.','.','.'],
				["O","O","O","."],
				[".","O",".","."],
				[".",".",".","."]]
	def penis270(self,x=0,y=0):
		self.center.setCoordinate(1,1)
		self.leftCorner.setCoordinate(x,y)
		self.symbolType = 'penis270'
		self.symbolFamily = 'Penis'
		return [['.','O','.','.'],
				["O","O",".","."],
				[".","O",".","."],
				[".",".",".","."]]
