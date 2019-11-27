
class connectedList:
    listA = []
    listB = []
    def __init__(self,listA,listB):
        for value in listB:
            if type(value) != int and type(value) != float:
                raise TypeError("Second param must consist of numbers")
        self.listA = listA.copy()
        self.listB = listB.copy()

    def printLists(self):
        print(self.listA)
        print(self.listB)
        
    def sortConnectedLists(self):
        #sorts both lists by values of listB
        #
        #e.g. ListA containing names and listB containing score
        #     so it sorts both by seconds list            
        consListA = self.listA.copy() 
        consListB = self.listB.copy()
        self.listA = []
        self.listB.sort()

        for i in self.listB:
            index = consListB.index(i)
            self.listA.append(consListA[index])
            consListA.pop(index)
            consListB.pop(index)