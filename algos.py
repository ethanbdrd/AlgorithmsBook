from userChoice import * 

"""
Function BubbleSort : Sort a list with a O(n²) complexity
Input : list tab -> number of x
Output : sorted list of x
"""
def bubbleSort(tab):
    for i in range(len(tab)):
        swapped = False #To optimize the complexity.
        for j in range(len(tab)-1-i):
            if tab[j]>tab[j+1]:
                tab[j], tab[j+1]= tab[j+1], tab[j]
                swapped = True
        if not swapped:  #If 0 swap, list already sorted
            break
    return tab

