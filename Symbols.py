from Coordinate import *
class Symbols:
	center = Coordinate(0,0)
	symbolType = ''
	
	def getSymbolType(self):
		return self.symbolType
	
	def getCenter(self):
		return self.center
	def four(self):
		self.center.setCoordinate(1,1)
		self.symbolType = 'four'
		return [[".",".",".","."],
				['O','O','O','O'],
				[".",".",".","."],
				[".",".",".","."]]

	def four90(self):
		self.center.setCoordinate(1,1)
		self.symbolType = 'four'
		return [[".","O",".","."],
				['.','O','.','.'],
				[".","O",".","."],
				[".","O",".","."]]

	def L(self):
		self.center.setCoordinate(1,1)		
		self.symbolType = 'L'
		return [['O','.','.','.'],
				["O","O","O","."],
				[".",".",".","."],
				[".",".",".","."]]

	def L90(self):
		self.center.setCoordinate(1,1)
		self.symbolType = 'L90'
		return [['.','O','O','.'],
				[".","O",".","."],
				[".","O",".","."],
				[".",".",".","."]]
	def L180(self):
		self.center.setCoordinate(1,1)
		self.symbolType = 'L180'
		return [['.','.','.','.'],
				["O","O","O","."],
				[".",".","O","."],
				[".",".",".","."]]
	def L270(self):
		self.center.setCoordinate(1,1)
		self.symbolType = 'L270'
		return [['.','O','.','.'],
				[".","O",".","."],
				["O","O",".","."],
				[".",".",".","."]]
		
	

	def revL(self):
		self.center.setCoordinate(1,1)
		self.symbolType = 'revL'
		return [['.','.','O','.'],
				["O","O","O","."],
				[".",".",".","."],
				[".",".",".","."]]

	def revL90(self):
		self.center.setCoordinate(1,1)
		self.symbolType = 'revL180'
		return [['.','O','.','.'],
				[".","O",".","."],
				[".","O","O","."],
				[".",".",".","."]]
	def revL180(self):
		self.center.setCoordinate(1,1)
		self.symbolType = 'revL180'
		return [['.','.','.','.'],
				["O","O","O","."],
				["O",".",".","."],
				[".",".",".","."]]
	def revL270(self):
		self.center.setCoordinate(1,1)
		self.symbolType = 'revL270'
		return [['O','O','.','.'],
				[".","O",".","."],
				[".","O",".","."],
				[".",".",".","."]]
	def cube(self):
		self.center.setCoordinate(1,1)
		self.symbolType = 'cube'
		return [['O','O','.','.'],
				["O","O",".","."],
				[".",".",".","."],
				[".",".",".","."]]

	def penis(self):
		self.center.setCoordinate(1,1)
		self.symbolType = 'penis'
		return [['.','O','.','.'],
				["O","O","O","."],
				[".",".",".","."],
				[".",".",".","."]]
	def penis90(self):
		self.center.setCoordinate(1,1)
		self.symbolType = 'penis90'
		return [['.','O','.','.'],
				[".","O","O","."],
				[".","O",".","."],
				[".",".",".","."]]
	def penis180(self):
		self.center.setCoordinate(1,1)
		self.symbolType = 'penis180'
		return [['.','.','.','.'],
				["O","O","O","."],
				[".","O",".","."],
				[".",".",".","."]]
	def penis270(self):
		self.center.setCoordinate(1,1)
		self.symbolType = 'penis270'
		return [['.','O','.','.'],
				["O","O",".","."],
				[".","O",".","."],
				[".",".",".","."]]
