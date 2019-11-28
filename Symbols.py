from Coordinate import *
class Symbols:
	center = Coordinate(0,0)
	symbolType = ''
	symbolFamily = ''
	def getSymbolType(self):
		return self.symbolType
	
	def getCenter(self):
		return self.center
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
