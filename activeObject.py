from Symbols import *
from Coordinate import *
from Board import *
from copy import *

class activeObject:
	symbol = []
	symbolBoard = []
	nextSymbolBoard = []
	symbolType = ''
	symbolFamily = ''
	center = Coordinate()
	leftCorner = Coordinate()
	sym=Symbols()

	Four = ('four','four90')
	L = ('L','L90','L180','L270')
	RevL = ('revL','revL90','revL180','revL270')
	Penis = ('penis','penis90','penis180','penis270')


	def __init__(self,symbol,sym):
		self.sym = sym
		self.symbol = symbol
		self.symbolBoard = initBoard()
		self.nextSymbolBoard = initBoard() 
		self.symbolType = sym.symbolType
		self.center = sym.getCenter()
		self.symbolFamily = sym.symbolFamily
		self.leftCorner = sym.leftCorner

		addToBoard(self.symbolBoard,symbol)
		addToBoard(self.nextSymbolBoard,symbol)
	def rotate(self,board):                #brace youselves for the shitties code written
		#if self.leftCorner.getY() >= 17: return          can be replace with try;except IndexError when called or same try;except inside the fun
		if self.symbolFamily == 'Cube':        #actually not that bad
			return
		elif self.symbolFamily == 'L':
			index = self.L.index(self.symbolType)
			index = (index + 1)%len(self.L)
			self.symbolType = self.L[index]                          
			self.symbol = self.sym.nameToSymbol(self.L[index])
		elif self.symbolFamily == 'RevL':
			index = self.RevL.index(self.symbolType)										# determine shape after rotation using tuples defined
			index = (index + 1)%len(self.RevL)												# on line 15 & setting new symbolType e.g. 'L' -> 'L90'
			self.symbolType = self.RevL[index]                          
			self.symbol = self.sym.nameToSymbol(self.RevL[index])          
		elif self.symbolFamily == 'Penis':											
			index = self.Penis.index(self.symbolType)					
			index = (index + 1)%len(self.Penis)
			self.symbolType = self.Penis[index]                          
			self.symbol = self.sym.nameToSymbol(self.Penis[index])
		elif self.symbolFamily == 'Four':            
			index = self.Four.index(self.symbolType)  									# REVIEW: lijepljenje preko
			index = (index + 1)%len(self.Four)                                  #     ali umjesto center koristiti rubni lijevi od 4x4 matrice (X)
			self.symbolType = self.Four[index]												# 
			self.symbol = self.sym.nameToSymbol(self.Four[index])           	

		lcx = self.leftCorner.getX()
		lcy = self.leftCorner.getY()
		self.nextSymbolBoard = deepcopy(self.symbolBoard)												# overwriting current symbol with rotated one
		for i in range(4):																		#FIXME: something doesnt work with RevL
			self.nextSymbolBoard[lcy+i]
			for j in range(4):
				self.nextSymbolBoard[lcy+i][lcx+j] = str(self.symbol[i][j])  
		
		if self.checkCollision(board):
			self.nextSymbolBoard = initBoard()  #discards all changes created by rotating
			return										#could be optimized by checking for collision before creating whole new board
		self.mergeBoards()							#...defining all rotated shape 'pixels' and checking if any of those are overlapping with 
															# 	 board


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
	
	def mergeBoards(self):									#merges nextSymBoard and symBoard
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
		self.center.drop()
		self.leftCorner.drop()
		print(self.center)
