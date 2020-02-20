import time
import threading
from random import randint
import os
from pynput.keyboard import Key, Listener
from pynput import keyboard
def boardInit(board,boardSize):
    w,h = boardSize
    row = []
    for i in range(w):
        row.append('.')
    for i in range(h):
        board.append(row)

def checkCooSaveBoard(saveboard,x,y):
    for k in saveboard:
        if k == coo(x,y):
            return True
    return False

def boardOutput(board,boardSize,dropobj,saveboard):
    w,h = boardSize
    for i in range(h):
        for j in range(w):
            if dropobj.contains(j,i): 
                print('*',end =' ')
            elif checkCooSaveBoard(saveboard,j,i):
                print('*',end = ' ')
            else: 
                print(board[i][j],end=' ')
        print(i)
class KeyQueue:
    queue = []
    
    @classmethod
    def clear(cls):
        while cls.queue: cls.queue.pop(0)

    @classmethod
    def isEmpty(cls):
        if not cls.queue: return True
        else: return False
    @classmethod
    def addToQueue(cls,key):
        cls.queue.append(key)
    
    @classmethod
    def removeFromQueue(cls):
        return cls.queue.pop(0)
class coo:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def down(self): self.y += 1
    def left(self): self.x -= 1
    def right(self): self.x += 1
    def getX(self): return self.x
    def getY(self): return self.y
    def __str__(self):
        x = str(self.x)
        y = str(self.y)
        return '('+x+','+y+')'
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y
class Shapes:
    L = [coo(0,0),coo(0,1),coo(0,2),coo(1,2)]
    L90 = [coo(0,0),coo(0,1),coo(1,0),coo(2,0)]
    L180 = [coo(0,0),coo(1,0),coo(1,1),coo(1,2)]
    L270 = [coo(2,0),coo(2,1),coo(1,1),coo(0,1)]

    revL = [coo(0,2),coo(1,2),coo(1,1),coo(1,0)]
    revL90 = [coo(0,0),coo(0,1),coo(1,1),coo(2,1)]
    revL180 = [coo(0,0),coo(0,1),coo(1,0),coo(0,2)]
    revL270 = [coo(0,0),coo(1,0),coo(2,0),coo(2,1)]

    penis = [coo(1,0),coo(1,1),coo(0,1),coo(2,1)]
    penis90 = [coo(0,0),coo(0,1),coo(0,2),coo(1,1)]
    penis180 = [coo(0,0),coo(1,0),coo(2,0),coo(1,1)]
    penis270 = [coo(0,1),coo(1,0),coo(1,1),coo(1,2)] 

    four = [coo(0,0),coo(0,1),coo(0,2),coo(0,3)]
    four90 = [coo(0,0),coo(1,0),coo(2,0),coo(3,0)]

    block = [coo(0,0),coo(0,1),coo(1,0),coo(1,1)]

    rotL = [L,L90,L180,L270]
    rotrevL = [revL,revL90,revL180,revL270]
    rotpenis = [penis,penis90,penis180,penis270]
    rotfour = [four,four90]
    rotblock = [block]

class DroppingObjects:     
    def __init__(self,shape,x=0,y=0):
        self.location = coo(x,y)
        self.containingPixels = shape.copy()
        self.currContainingPixels = []
        for i in self.containingPixels:
            ix = i.getX()
            iy = i.getY()
            self.currContainingPixels.append(coo(x+ix,y+iy))
    
    def reinit(self,shape):
        self.containingPixels = shape.copy()
        self.currContainingPixels = []
        for i in self.containingPixels:
            ix = i.getX() + self.location.getX()
            iy = i.getY() + self.location.getY()
            self.currContainingPixels.append(coo(ix,iy))
    
    def contains(self,x,y):
        for i in self.currContainingPixels:
            if i == coo(x,y):
                return True
        return False
    
    def down(self):
        for i in self.currContainingPixels:
            i.down()
        self.location.down()
    
    def right(self,saveboard):
        for i in self.currContainingPixels:
            if i.getX()+1>8-1 or coo(i.getX()+1,i.getY()) in saveboard:  
                return False
        for i in self.currContainingPixels:
            i.right()
        self.location.right()
    
    def left(self,saveboard):
        for i in self.currContainingPixels:
            if i.getX()-1<0 or coo(i.getX()-1,i.getY()) in saveboard:  
                return False
        for i in self.currContainingPixels:
            i.left()
        self.location.left()
    
    def isDropped(self,boardSize,saveboard):
        h = boardSize[1]
        nextLocationPixels = []
        for i in self.currContainingPixels:
            if i.getY() == h-1: #-1 brojanje krece od 0
                return True
            nextY = i.getY()+1
            nextX = i.getX()
            if coo(nextX,nextY) in saveboard:
                return True
        return False
    
    def isEnd(self,saveboard,boardSize):
        for i in self.currContainingPixels:
            if i.getY() == 0 and self.isDropped(boardSize,saveboard):
                return True
        return False

def on_release(key):
    KeyQueue.addToQueue(key)

def randomShape():
    randomShape = randint(0,4)
    shapeFamily,currentShape = None,None
    if randomShape == 0:
        shapeFamily = Shapes.rotL
        currentShape = Shapes.L
    elif randomShape == 1:
        shapeFamily = Shapes.rotrevL
        currentShape = Shapes.revL
    elif randomShape == 2:
        shapeFamily = Shapes.rotfour
        currentShape = Shapes.four
    elif randomShape == 3:
        shapeFamily = Shapes.rotblock
        currentShape = Shapes.block
    elif randomShape == 4:
        shapeFamily = Shapes.rotpenis
        currentShape = Shapes.penis
    return currentShape,shapeFamily

def rotate(currentShape,shapeFamily,dropobj):
    familyLen = len(shapeFamily)
    for i,k in enumerate(shapeFamily):
        if k == currentShape:
            currentShape = shapeFamily[(i+1)%familyLen]
            dropobj.reinit(currentShape)
            return currentShape

def checkIfFullRow(saveboard):
    row = [0 for i in range(15)]
    full_rows = []
    for i in saveboard:
        row[i.getY()] += 1
    for k,i in enumerate(row):
        if i == 8:
            full_rows.append(k)
    
    toBeRemoved = []

    for i in full_rows:
        for j in saveboard:
            if int(i) == int(j.getY()):
                toBeRemoved.append(j)
    for i in toBeRemoved:
        saveboard.remove(i)

    full_rows.sort()
    for i in full_rows:
        for j in saveboard:
            if j.getY()<i:
                j.down()
    if not full_rows:
        return 0
    else:
        return len(full_rows)
def cls():
    os.system('clear') #UNIX

def mainThread():
    boardSize = (8,15) #(w,h)
    board = []
    saveboard = []
    currentShape,shapeFamily = randomShape()
    dropobj = DroppingObjects(currentShape)
    boardInit(board,boardSize)
    score = 0
    cls()
    print("SCORE:",score)
    boardOutput(board,boardSize,dropobj,saveboard)
    while True:
        while not dropobj.isDropped(boardSize,saveboard):
            time.sleep(0.5)
            if not KeyQueue.isEmpty(): 
                instruction = KeyQueue.removeFromQueue()
                if instruction == Key.left: 
                    dropobj.left(saveboard)
                    dropobj.down()
                elif instruction == Key.right: 
                    dropobj.right(saveboard)
                    dropobj.down()
                elif instruction == Key.up:
                    currentShape = rotate(currentShape,shapeFamily,dropobj)
                    dropobj.down()
                elif instruction == Key.esc:
                    break
            else: 
                if not dropobj.isDropped(boardSize,saveboard):
                    dropobj.down()
            cls()
            print("SCORE:",score)
            boardOutput(board,boardSize,dropobj,saveboard)
        #saveboard and shit
        KeyQueue.clear()
        score +=  10
        for i in dropobj.currContainingPixels:
            saveboard.append(i)
        currentShape,shapeFamily = randomShape()
        dropobj = DroppingObjects(currentShape)
        if (dropobj.isEnd(saveboard,boardSize)):
            print("*"*10,"END SCORE",score,"*"*10)
            for a_thread in threading.enumerate():
                try:a_thread.kill()
                except AttributeError:
                    os._exit(1)
                print(a_thread,'is killed')
            
            break
        score += checkIfFullRow(saveboard)*100
    

def main():
    IKeyQueue = KeyQueue()
    os.system("stty -echo")
    x = threading.Thread(target=mainThread)
    x.start()
    with keyboard.Listener(on_release=on_release) as listener:
        listener.join()
         



if __name__=='__main__': 
    main()
