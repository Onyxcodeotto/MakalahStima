class Route:
    def __init__(self, other = None):
        if other == None:
            self.buffer = []
        else:
            self.buffer = other.GetBuffer().copy()
    def __str__(self):
        return str(self.buffer)
    def addNode(self,node):
        self.buffer += [node]
        
    def isExists(self,node):
        for i in self.buffer:
            if(i == node):
                return True 
        return False
    def GetBuffer(self):
        return self.buffer
    def GetLast(self):
        return self.buffer[-1]
    def GetLength(self):
        return len(self.buffer)
    