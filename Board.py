def initBoard():
	h,w = 20,8
	a = [['.' for x in range(w)] for y in range(h)]
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
