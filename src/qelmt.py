import numpy as np
from route import Route
import pandas as pd
class Elmt:
    def __init__(self,  matrix, node,rute : Route, cost, start):
        self.matrix = matrix
        self.node = node
        self.rute = rute
        
        if(cost == 0):
            self.rute.addNode(node)
            self.cost = self.calculateCost(cost)
        else:
            realCost = self.matrix.at[self.rute.GetLast(),self.node]
            self.matrix = self.matrix.drop(node, axis = 1)
            self.matrix = self.matrix.drop(self.rute.GetLast(), axis = 0)
            if(self.node!= start):
                temp = self.matrix.at[self.node,start]
                self.matrix.at[self.node,start] = 999999
            
            
            if len(self.matrix) ==1:
                self.cost = cost + realCost
            else:
                self.cost = self.calculateCost(cost) + realCost
            if(self.node!= start):
                self.matrix.at[self.node,start] = temp
            self.rute.addNode(node)
        
    def __lt__(self, other):
        return self.cost<other.cost
    def __eq__(self, other):
        return self.cost == other.cost
    def GetNode(self):
        return self.node
    def GetRoute(self):
        return self.rute
    def GetCost(self):
        return self.cost
    def GetMatrix(self):
        return self.matrix
    def IsSolution(self):
        return self.matrix.empty
    def calculateCost(self, cost):
        minRow = self.subtractRow()
        minColumn = self.matrix.min()
        self.matrix = self.matrix.subtract(minColumn ,axis=1)
        return minRow + minColumn.sum()+ cost
    def subtractRow(self):
        total = 0
        for i in range(len(self.matrix)):
            
            min = self.matrix.at[self.matrix.index[i],self.matrix.columns[0]]
            for j in range(1, len(self.matrix.columns)):
                temp = self.matrix.at[self.matrix.index[i],self.matrix.columns[0]]
                if(min>self.matrix.at[self.matrix.index[i],self.matrix.columns[j]]):
                    min = self.matrix.at[self.matrix.index[i],self.matrix.columns[j]]
            for j in range(len(self.matrix)):
                self.matrix.at[self.matrix.index[i],self.matrix.columns[j]] -= min        
            total += min
        return total
        

    
                        
        
                        
                        
                    
                        
                    
                        
                    
                
    