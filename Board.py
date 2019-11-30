class Board:
	height = 20
	width = 8
	@classmethod
	def getWidth(cls): return cls.width
	@classmethod
	def getHeight(cls): return cls.height

def initBoard():
		a = [['.' for x in range(Board.width)] for y in range(Board.height)]
		return a

def drawBoard(board):
	#os.system("clear")
	for i in range(len(board)):
		for j in range(len(board[0])):
			print(board[i][j], end="  ")
		print("\n")

def addToBoard(board,elem):
	rows = len(elem)
	columns = len(elem[0])
	#print(rows,columns)
	for row in range(rows):
		for column in range(columns):
			if elem[row][column] == 'O':
				board[row][column] = 'O'
