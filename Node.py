class Node:
    def __init__(self):
        self.data=0
        self.nextPtr=None

    def setData(self,data):
        self.data=data
    def getData(self):
        return self.data

    def setNextPtr(self,nextPtr):
        self.nextPtr=nextPtr
    def getNextPtr(self):
        return self.nextPtr