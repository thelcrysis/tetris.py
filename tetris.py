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
	standardST = 2500
	st = standardST
	cst = standardST
	i=19    #number of rows --- used to determining if its time to generate new object TODO: replace with a flag
	while(True):
		if cst == st:
			displayBoard = initBoard()
			cst = 0
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
				cst = st
				print("i 19")
				continue
			else:
				print("Not fallen!")
		
			active.refreshNextBoard()
			print("Refreshed")
			if (active.checkCollision(board)):
				addToBoard(board,active.getBoard())
				i = 19
				cst = st

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
			## trying out rotates
			randominteger = random.randint(1,5)
			if randominteger == 3:
				#print('rotato' + active.leftCorner.__str__())
				try:
					active.rotate(board)
				except IndexError:
					pass
			#print("Display")
		time.sleep(0.0001)
		cst += 1
		i=i+1
if __name__=="__main__":
	main()	
