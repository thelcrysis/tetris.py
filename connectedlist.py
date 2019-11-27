
class connectedList:
    listA = []
    listB = []
    def __init__(self,listA,listB):
        for value in listB:
            if type(value) != int and type(value) != float:
                raise TypeError("Second param must consist of numbers")
        self.listA = listA.copy()
        self.listB = listB.copy()
    @staticmethod
    def testdefine():
        a = [40,60,70,30,20,50,10]
        b = ['d','f','g','c','b','e','a']
        c = [4,6,7,3,2,5,1]
        return a,b,c
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
    @staticmethod
    def sortMulConnectedLists(*args):
        #checking if every param is of right type
        args = list(args)
        for arg in args:
            if type(arg) != list:
                raise TypeError("params must be lists")
        sortingListIndex = len(args)-1
        sortingList = args.pop(sortingListIndex)
        for value in sortingList:
            if type(value) != int and type(value) != float:
                raise TypeError("Second param must consist of numbers")

        consLists = []
        resultLists = []
        for arg in args:
            resultLists.append([])
            consLists.append(arg)
        consSortingList = sortingList.copy()
        sortingList.sort()
        
        for i in sortingList:
            index = consSortingList.index(i)
            for j in range(len(resultLists)):
                resultLists[j].append(consLists[j][index])
                consLists[j].pop(index)
            consSortingList.pop(index)
        resultLists.append(sortingList)
        return resultLists        