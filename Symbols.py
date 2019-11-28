from Coordinate import *
class Symbols:
	center = Coordinate(0,0)
	leftCorner = Coordinate(0,0)
	symbolType = ''
	symbolFamily = ''
	def getSymbolType(self):
		return self.symbolType
	
	def getCenter(self):
		return self.center
	def nameToSymbol(self,name):
		if name == 'four': return self.four()
		elif name == 'four90': return self.four90()
		elif name == 'L': return self.L()
		elif name == 'L90': return self.L90()
		elif name == 'L180': return self.L180()
		elif name == 'L270': return self.L270()
		elif name == 'revL': return self.revL()
		elif name == 'revL90': return self.revL90()
		elif name == 'revL180': return self.revL180()
		elif name == 'revL270': return self.revL270()
		elif name == 'penis': return self.penis()
		elif name == 'penis90': return self.penis90()
		elif name == 'penis180': return self.penis180()
		elif name == 'penis270': return self.penis270()
		elif name == 'cube': return self.cube()

	def four(self):
		self.center.setCoordinate(1,1)
		self.symbolType = 'four'
		self.symbolFamily = 'Four'
		return [[".",".",".","."],
				['O','O','O','O'],
				[".",".",".","."],
				[".",".",".","."]]

	def four90(self):
		self.center.setCoordinate(1,1)
		self.symbolType = 'four'
		self.symbolFamily = 'Four'
		return [[".","O",".","."],
				['.','O','.','.'],
				[".","O",".","."],
				[".","O",".","."]]

	def L(self):
		self.center.setCoordinate(1,1)		
		self.symbolType = 'L'
		self.symbolFamily = 'L'

		return [['O','.','.','.'],
				["O","O","O","."],
				[".",".",".","."],
				[".",".",".","."]]

	def L90(self):
		self.center.setCoordinate(1,1)
		self.symbolType = 'L90'
		self.symbolFamily = 'L'
		return [['.','O','O','.'],
				[".","O",".","."],
				[".","O",".","."],
				[".",".",".","."]]
	def L180(self):
		self.center.setCoordinate(1,1)
		self.symbolType = 'L180'
		self.symbolFamily = 'L'
		return [['.','.','.','.'],
				["O","O","O","."],
				[".",".","O","."],
				[".",".",".","."]]
	def L270(self):
		self.center.setCoordinate(1,1)
		self.symbolType = 'L270'
		self.symbolFamily = 'L'
		return [['.','O','.','.'],
				[".","O",".","."],
				["O","O",".","."],
				[".",".",".","."]]
		
	

	def revL(self):
		self.center.setCoordinate(1,1)
		self.symbolType = 'revL'
		self.symbolFamily = 'RevL'
		
		return [['.','.','O','.'],
				["O","O","O","."],
				[".",".",".","."],
				[".",".",".","."]]

	def revL90(self):
		self.center.setCoordinate(1,1)
		self.symbolType = 'revL180'
		self.symbolFamily = 'RevL'
		return [['.','O','.','.'],
				[".","O",".","."],
				[".","O","O","."],
				[".",".",".","."]]
	def revL180(self):
		self.center.setCoordinate(1,1)
		self.symbolType = 'revL180'
		self.symbolFamily = 'RevL'
		return [['.','.','.','.'],
				["O","O","O","."],
				["O",".",".","."],
				[".",".",".","."]]
	def revL270(self):
		self.center.setCoordinate(1,1)
		self.symbolType = 'revL270'
		self.symbolFamily = 'RevL'
		return [['O','O','.','.'],
				[".","O",".","."],
				[".","O",".","."],
				[".",".",".","."]]
	def cube(self):
		self.center.setCoordinate(1,1)
		self.symbolType = 'cube'
		self.symbolType = 'Cube'
		
		return [['O','O','.','.'],
				["O","O",".","."],
				[".",".",".","."],
				[".",".",".","."]]

	def penis(self):
		self.center.setCoordinate(1,1)
		self.symbolType = 'penis'
		self.symbolFamily = 'Penis'

		return [['.','O','.','.'],
				["O","O","O","."],
				[".",".",".","."],
				[".",".",".","."]]
	def penis90(self):
		self.center.setCoordinate(1,1)
		self.symbolType = 'penis90'
		self.symbolFamily = 'Penis'
		return [['.','O','.','.'],
				[".","O","O","."],
				[".","O",".","."],
				[".",".",".","."]]
	def penis180(self):
		self.center.setCoordinate(1,1)
		self.symbolType = 'penis180'
		self.symbolFamily = 'Penis'
		return [['.','.','.','.'],
				["O","O","O","."],
				[".","O",".","."],
				[".",".",".","."]]
	def penis270(self):
		self.center.setCoordinate(1,1)
		self.symbolType = 'penis270'
		self.symbolFamily = 'Penis'
		return [['.','O','.','.'],
				["O","O",".","."],
				[".","O",".","."],
				[".",".",".","."]]
