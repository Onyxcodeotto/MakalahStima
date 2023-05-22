import numpy as np
import pandas as pd
import os
import openpyxl
from queue import PriorityQueue
from qelmt import Elmt
from route import Route

def loadData(filepath):
    try:
        df = pd.read_excel(filepath, sheet_name="Sheet1")
        column = df.columns.to_list()
        array = df.to_numpy()
        
        return column[1:], array[:,1: df.shape[0]]
    except SyntaxError:
        print("File input error")
def loadData2(filepath):
    df = pd.read_excel(filepath, sheet_name="Sheet1")
    return df
def getRoute(start, df):
    df = df[df.columns.drop(list(df.filter(regex='Test')))]
    df = swap(df, 0,df.columns.get_loc(start)-1)
    df = df.set_index('other_village')
    
    df = setInf(df)
    
    
    q = PriorityQueue()
    element = Elmt(df, start, Route(), 0, start)
    q.put(element)
    best = np.inf
    while(not q.empty()):
        element = q.get()
        # print(element.GetMatrix())
        # print(element.GetCost())
        print(element.GetRoute())
        previous = element.GetRoute().GetLast()
        if(element.IsSolution()):
            if(element.GetCost()<best):
                best = element.GetCost()
                otherq = PriorityQueue()
                while(not q.empty()):
                    temp = q.get()
                    if(best<temp.GetCost()):
                        while not q.empty:
                            q.get()
                    else:
                        otherq.put(temp)
                while(not otherq.empty()):
                    q.put(otherq.get())
        else:
            for i in range(len(element.GetMatrix().loc[previous])):
                if (element.GetRoute().GetLength()<= len(df)-1 and i!=0) or (element.GetRoute().GetLength()> len(df)-1 and i==0):
                    q.put(Elmt(element.GetMatrix().copy(), element.GetMatrix().columns[i], Route(element.GetRoute()), element.GetCost(),start))
    return element
                
            
                
    
    
    

# def reduceMatrix(matrix, asal, tujuan):
#    count = 0
#     for i in range(len(matrix)):
        
def setInf(df):
    df = df.replace(999999, np.inf)
    return df   

def reduceMatrixInit(matrix):
    matrix, rowSum = subtractRow(matrix)
    minColumn = matrix.min()
    matrix = matrix.subtract(minColumn ,axis=1)
    #subtract column
    

    return matrix, rowSum+ minColumn.sum()
        
def subtractRow(matrix):
    total = 0
    for i in range(len(matrix)):
        min = matrix.at[matrix.columns[i],matrix.columns[0]]
        for j in range(1, len(matrix)):
            temp = matrix.at[matrix.columns[i],matrix.columns[0]]
            if(min>matrix.at[matrix.columns[i],matrix.columns[j]]):
                min = matrix.at[matrix.columns[i],matrix.columns[j]]
        for j in range(len(matrix)):
            matrix.at[matrix.columns[i],matrix.columns[j]] -= min        
        total += min
    return matrix, total
                
def swap(df, x1, x2):
    df.iloc[x1], df.iloc[x2]= df.iloc[x2].copy(), df.iloc[x1].copy() 
    column = list(df.columns)
    column[x1+1], column[x2+1] = column[x2+1], column[x1+1]
    df = df[column]    
    print(df)
    return df
command = "random"
while(command != "exit"):
    print("Rute Farm Noble Line")
    print("Untuk game Mount and Blade 2: Bannerlord")         
    print("Pilih faksi:")
    print("Tersedia")
    print("1. Vlandia")

    print("Belum Tersedia")
    print("2. Khuzait")
    print("3. Aserai")
    print("4. Battania")
    print("5. Sturgia")
    print("6. Empire ")
    print("0. Exit")
    command = input("Input fraksi (namanya): ").lower()

    if command == "vlandia":
        data = loadData2("./inputfile/vlandia_time_speed.xlsx")
    elif command == "exit":
        command = "exit" # do nothing
    elif command == "test":
        data = loadData2("./inputfile/test.xlsx")
    else:
        print("input error")
        continue
    valid = False
    while not valid:
        print("Masukkan asal desa (angka)")
        for i in range(1,len(data.columns)):
            print(str(i)+". "+data.columns[i])
        try:
            command = int(input("Input: "))
            if(command<1 or command>len(data.columns)):
                raise
            valid = True
        except:
            print("Input salah")
    start = data.columns[command]
            
            
    result = getRoute(start, data)
    print("Rute: " +str(result.GetRoute()))
    print("Lama dalam kecepatan maksimum 8.2= "+ str(result.GetCost()))
    
    

    







