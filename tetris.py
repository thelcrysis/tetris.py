import os
import time
import random
from copy import copy, deepcopy
import curses #not used as of yet
from pynput.keyboard import Key, Controller #not used as of yet
import random
#my modules
from Coordinate import *
from Symbols import *
from activeObject import *

			

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

def newObject(sym): #random generates objects that are going to drop

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
	active = activeObject(shape,sym)
	return active

def main():

	board = []
	board = initBoard()

	sym = Symbols()
	standardST = 5000
	st = standardST
	cst = standardST
	i=19    #number of rows --- used to determining if its time to generate new object TODO: replace with a flag
	while(True):
		if cst == st:
			displayBoard = initBoard()
			cst = 0
			if i==19:
				active = newObject(sym)
				#print("Made new object and checking for end...")
				if (active.checkCollision(board)):
					#print("END detected, quitting...")
					break
				i=0
				continue
				## trying out rotates
			randominteger = random.randint(1,10)
			outputmove = ''
			if randominteger in [3,5,7,9]:
				try:
					active.rotate(board)
					outputmove += '| Rotate' 
				except IndexError:
					pass
			if randominteger >0:
				try:
					active.moveHorizontally(board,'left')
					outputmove += '| Left'
				except IndexError:
					pass
			#if randominteger in [6,8]:
			#	try:
			#		active.moveHorizontally(board,'right')
			#		print('right')
			#	except IndexError:
			#		print('INDEXXX')
			#		pass
				
			

			if (active.checkIfFallen()):
				addToBoard(board,active.getBoard())
				
				i = 19
				cst = st
				#print("i 19")
				continue
			else:
				#print("Not fallen!")
				pass
			active.refreshNextBoard()
			#print("Refreshed")
			if (active.checkCollision(board)):
				addToBoard(board,active.getBoard())
				i = 19
				cst = st

				#print("Collision!")
				continue
			else:
				#print("MERGED")
				active.mergeBoards()
			
			addToBoard(displayBoard,board)
			addToBoard(displayBoard,active.getBoard())
			#print(time.gmtime())
			drawBoard(displayBoard)
			print("----------------------INFO-------------------------")
			print(outputmove)
			output1 = "%10s | %10s | %10s" % ('leftCorner','shapeLeft','shapeRight')
			outputb = "%10s | %10s | %10s" % (str(active.leftCorner.x),str(active.shapeLeftCorner.x),str(active.shapeRightCorner.x))
			print(output1)
			print(outputb)
			#drawBoard(board)
			
		time.sleep(0.0001)
		cst += 1
		i=i+1
if __name__=="__main__":
	main()	
