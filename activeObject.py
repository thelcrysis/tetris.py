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
	shapeLeftCorner = Coordinate()
	shapeRightCorner = Coordinate()

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
		self.shapeRightCorner = sym.shapeRightCorner
		self.shapeLeftCorner = sym.shapeLeftCorner

		addToBoard(self.symbolBoard,symbol)
		addToBoard(self.nextSymbolBoard,symbol)
																														# ** return is done by directly altering objects
		
	def overwriteSymbolRotate(self,board):
		lcx = self.leftCorner.getX()
		lcy = self.leftCorner.getY()
		self.nextSymbolBoard = deepcopy(self.symbolBoard)												# overwriting current symbol with a new one
		for i in range(4):																						# used by rotate and will be used with left and right
			for j in range(4):																					# nextSymbol board, usually mergeBoard() needed
				self.nextSymbolBoard[lcy+i][lcx+j] = str(self.symbol[i][j])  						# after || CANNOT BE USED FOR THIS
		if self.checkCollision(board):
			self.nextSymbolBoard = initBoard()  
			return False
		else: return True

	def checkIfOutside(self,side):
		deltaPosition = -1 if side == 'left' else 1
		if not self.sym.shapeLeftCorner.x+deltaPosition>=0 or self.sym.shapeRightCorner.x+deltaPosition>Board.getWidth(): #-1 bc gedWidthislen and we need last index
			return True
		else: return False

	def checkIfPixelOutside(self,x):
		if x<0 or x>Board.getWidth()-1:
			return True
		else: return False

	def moveHorizontally(self,board,side='left'):
		if side not in ['left','right']: raise TypeError("param 'side' must be equal to 'left' or right")
		
		lcx = self.leftCorner.getX()		#part that should be erased aka replaced with dots
		rcx = lcx + 3
		if self.checkIfOutside(side): return
		else:
			if side=='left': 
				self.leftCorner.left()
				self.shapeRightCorner.left()
				self.shapeLeftCorner.left()
				print('tu same')

			else: 
				self.leftCorner.right()
				self.shapeLeftCorner.right()
				self.shapeRightCorner.right()

		lcy2 = self.leftCorner.getY()							#TODO:restrict left and right
		new_lcx = self.leftCorner.getX()						#TODO: make left and right work 
																		#last change... erasing symbol from previous position (curr not working)
		if self.checkIfOutside(side): return
		self.nextSymbolBoard = deepcopy(self.symbolBoard)
		for i in range(4):
			for j in range(4):
				self.nextSymbolBoard[lcy2+i][lcx+j] = '.'				#erases symbol from original position
		for i in range(4):

			for j in range(4):
				if not self.checkIfPixelOutside(new_lcx+j):
					self.nextSymbolBoard[lcy2+i][new_lcx+j] = str(self.symbol[i][j])
				
		if self.checkCollision(board):
			self.nextSymbolBoard = initBoard()
			
			return False
		self.mergeBoards()

		print(self.leftCorner)


	def rotate(self,board):                #brace youselves for the shitties code written
		#if self.leftCorner.getY() >= 17: return          can be replace with try;except IndexError when called or same try;except inside the fun
		old_symbol = Symbols()
		old_symbol.symbolType = self.symbolType
		old_symbol.symbol = self.symbol
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
		self.leftCorner = self.sym.leftCorner
		self.shapeLeftCorner = self.sym.shapeLeftCorner
		self.shapeRightCorner = self.sym.shapeRightCorner
		print('UPDATE',self.leftCorner,self.shapeLeftCorner,self.shapeRightCorner)
		
		if not self.sym.shapeLeftCorner.x>=0 or self.sym.shapeRightCorner.x>Board.getWidth()-1:
			self.symbolType = old_symbol.symbolType
			self.symbol = old_symbol.symbolType
			return False
			
		##update info

		if self.overwriteSymbolRotate(board):
			self.mergeBoards()							
											#could be optimized by checking for collision before creating whole new board
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
