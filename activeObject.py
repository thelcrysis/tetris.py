from Symbols import *
from Coordinate import *
from Board import *

class activeObject:
	symbol = []
	symbolBoard = []
	nextSymbolBoard = []
	symbolType = ''
	symbolFamily = ''
	center = Coordinate(0,0)
	sym=Symbols()

	Four = ('four','four90')
	L = ('L','L90','L180','L270')
	RevL = ('revL','revL90','revL180','revL270')
	Penis = ('penis','penis90','penis180','penis270')


	def __init__(self,symbol,sym):
		self.sym = sym
		self.symbol = symbol
		self.symbolBoard = initBoard()
		self.nextSymbolBoard = initBoard() #WARNI
		self.symbolType = sym.symbolType
		self.center = sym.getCenter()
		self.symbolFamily = sym.symbolFamily

		addToBoard(self.symbolBoard,symbol)
		addToBoard(self.nextSymbolBoard,symbol)
	def rotate(self):                #brace youselves for the shitties code written
		
		if self.symbolFamily == 'Cube':        #actually not that bad
			pass
		elif self.symbolFamily == 'L':
			index = self.L.index(self.symbolType)
			index = (index + 1)%len(self.L)
			self.symbol = self.sym.nameToSymbol(self.L[index])
		elif self.symbolFamily == 'RevL':
			index = self.RevL.index(self.symbolType)
			index = (index + 1)%len(self.RevL)
			self.symbol = self.sym.nameToSymbol(self.RevL[index])          
		elif self.symbolFamily == 'Penis':
			index = self.Penis.index(self.symbolType)
			index = (index + 1)%len(self.Penis)
			self.symbol = self.sym.nameToSymbol(self.Penis[index])
		elif self.symbolFamily == 'Four':                                 		# TODO:finish rotate() 
			index = self.Four.index(self.symbolType)                            #     zalijepiti novi simbol preko postojeceg koristeci info iz center
			index = (index + 1)%len(self.Four)                                  #     ali umjesto center koristiti rubni lijevi od 4x4 matrice (X)
			self.symbol = self.sym.nameToSymbol(self.Four[index])           	#     - mozda definirati tu poziciju u Symbols (./)
	def getBoard(self):                                                  		# FIXME:missing Symbol.symboltype change 
																				# 	  - dodati zamijenu symboltype... inace ne moze rotirati vise od jednom (X)
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
		self.center.drop()
		print(self.center)
