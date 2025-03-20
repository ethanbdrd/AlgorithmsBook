from userChoice import * 
from algos import *


"""
main function : Take user inputs to execute the algorithm he want.
"""
def main():
    res = input("Which algorithm do you want to execute?")
    match res:
        case "0":
            res = input("Do you want to choose your input list ?(y/n)")
            list = mainRandomInts() if res=="y" else randomInts(100,0,1000,True)
            print("Input list : "+str(list))
            print("Sorted list :"+str(bubbleSort(list)))
        case "exit":
            print("Okay, bye !")
            return 
        case _:
            print("error, please try again.")
    main()

main()