import os
import time
#import keyboard
import random
from copy import copy, deepcopy

def initBoard():
	h,w = 20,8
	a = [['.' for x in range(w)] for y in range(h)]
	return a

def drawBoard(board):
	#os.system("clear")
	for i in range(20):
		for j in range(8):
			print(board[i][j], end="  ")
		print("\n")
	


	
class Coordinate:
	x = 0
	y = 0
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def setCoordinate(self,x,y):
		self.x = x
		self.y = y

class Symbols:
	center = Coordinate(0,0)
	symbolType = ''
	
	def getSymbolType(self):
		return self.symbolType

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

class activeObject:
	symbol = []
	symbolBoard = []
	nextSymbolBoard = []
	symbolType = ''
	center = Coordinate(0,0)
	def __init__(self,symbol,symType):
		self.symbol = symbol
		self.symbolBoard = initBoard()
		self.nextSymbolBoard = initBoard()
		self.symbolType = symType
		addToBoard(self.symbolBoard,symbol)
		addToBoard(self.nextSymbolBoard,symbol)

	
	def getBoard(self):
		return self.symbolBoard

	def checkCollision(self,board):
		for i in range(19,-1,-1):
			for j in range(7,-1,-1):
				if (str(board[i][j]) == str(self.nextSymbolBoard[i][j]) and str(board[i][j])=='O'):
					return True
		return False
	
	def checkIfFallen(self):
		for i in range(8):
			if str(self.symbolBoard[19][i]) == 'O':
				return True
		return False
	def mergeBoards(self):
		self.symbolBoard = deepcopy(self.nextSymbolBoard)
	#refresha nextSymbolBoard nakon cega bi trebalo provjeriti koliziju i mergati s symBoardom
	def refreshNextBoard(self): #TODO:optimizirati da ne prolazi po cijeloj ploci pomocu centra
		for i in range(19,-1,-1):
			for j in range(7,-1,-1):
				if i-1>=0:
					a = str(self.symbolBoard[i-1][j])
				else:
					a = '.'
				self.nextSymbolBoard[i][j] = a
		
def addToBoard(board,elem):
	rows = len(elem)
	columns = len(elem[0])
	#print(rows,columns)
	for row in range(rows):
		for column in range(columns):
			if elem[row][column] == 'O':
				board[row][column] = 'O'
			

#def refreshBoard(board):
#	a = ''
#	for i in range(19,-1,-1):
#		for j in range(7,-1,-1):
#			if str(board[i][j]) != 'O':
#				if (i-1)>=0:
#					a = str(board[i-1][j])
#					board[i-1][j] = '.'
#
#			
#					board[i][j] = a
#				#board[i][j] = 'a'
#				#drawBoard(board)
#				#time.sleep(0.01)

def newObject(sym):

	rand = random.randint(1,6)
	#wonky af switch case
	if rand == 1:
		shape = sym.four()
	elif rand == 2:
		shape = sym.L()
	elif rand == 3:
		shape = sym.L90()
	elif rand == 4:
		shape = sym.revL()
	elif rand == 5:
		shape = sym.cube()
	elif rand == 6:
		shape = sym.penis() 
	symType = sym.getSymbolType() 
	active = activeObject(shape,symType)
	return active

def main():
	board = []
	board = initBoard()

	sym = Symbols()
	
	
	i=19
	while(True):
		displayBoard = initBoard()
		#inits board &&& and used as git explanation

		if i==19:
			active = newObject(sym)
			print("Made new object and checking for end...")
			if (active.checkCollision(board)):
				print("END detected, quitting...")
				break
			i=0
			continue
		if (active.checkIfFallen()):
			addToBoard(board,active.getBoard())
			#while (True):
			#	drawBoard(board)
			#	print("\n")
			print("Fallen!")
			i = 19
			continue
		else:
			print("Not fallen!")
		#if keyboard.is_pressed('k'):
		#	print("Yey detected it!")
		#	while not active.checkIfFallen() and not active.checkCollision(board):
		#		active.refreshNextBoard()
		#		if not active.checkIfFallen() and not active.checkCollision(board):
		#			active.mergeBoards()

		active.refreshNextBoard()
		print("Refreshed")
		if (active.checkCollision(board)):
			addToBoard(board,active.getBoard())
			i = 19
			print("Collision!")
			continue
		else:
			print("MERGED")
			active.mergeBoards()
		addToBoard(displayBoard,board)
		addToBoard(displayBoard,active.getBoard())
		print(time.gmtime())
		print("----------------------_dispBOARD_-------------------------")

		drawBoard(displayBoard)
		print("----------------------_BOARD_-------------------------")
		#drawBoard(board)

		#print("Display")
		time.sleep(0.12)

		i=i+1

if __name__=="__main__":
	main()	
