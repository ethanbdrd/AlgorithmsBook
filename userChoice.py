from random import *

"""
Function randomInts : return a random integer/list of integer with unique elements or no
Input : int n -> number of int
        int min -> minimum int possible
        int max -> maximum int possible
        boolean unnique -> can have same numbers in returned list
Output : int/integer list
"""    
def randomInts(n,min,max,unique):
    if n==1: #just one integer is asked
        return randint(min,max)
    if unique: #we must have unique int
        #create a list with all the possibilities and shuffle it
        tab=[i for i in range(min,max+1)] 
        shuffle(tab)
        if max-min+1==n: #len(tab)==n
            return tab
        else:
            #pick n elements from the list and return them
            tabRes=[]
            for _ in range(n):
                tabRes.append(tab.pop())
            return tabRes
    #pick n elements in [min,max] and return them
    tab=[]
    for _ in range(n):
        tab.append(randint(min,max))
    return tab

"""
mainRandomInts :execute de fonction randomInts with inputs to user
"""
def mainRandomInts():
    num = input("how many variables?")
    x = input("x min?")
    y = input("x max?")
    bool = input("Different variables or not? (y/n)")
    return randomInts(int(num),int(x),int(y),True if bool=="y" else False)