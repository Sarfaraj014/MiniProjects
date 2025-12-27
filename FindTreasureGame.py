''' it is a treasure game....
    1    2    3
1["🕵️‍♀️","🕵️‍♀️","🕵️‍♀️"]
2["🕵️‍♀️","🕵️‍♀️","🕵️‍♀️"]
3["🕵️‍♀️","🕵️‍♀️","🕵️‍♀️"]
'''
#            0               1               2
# ["🕵️‍♀️","🕵️‍♀️","🕵️‍♀️"]["🕵️‍♀️","🕵️‍♀️","🕵️‍♀️"]["🕵️‍♀️","🕵️‍♀️","🕵️‍♀️"]
import sys
import random
computerchoice=random.choice([11,12,13,21,22,23,31,32,33])
print(computerchoice)
list1=["🏠","🏠","🏠"]
list2=["🏠","🏠","🏠"]
list3=["🏠","🏠","🏠"]
nestedMearge=(list1,list2,list3)
print(f"{list1}\n{list2}\n{list3}")
#------------------------------first choice-------------------------
userinput=input("enter your 1st choice : ")
row=int(userinput[0])-1
column=int(userinput[1])-1
#----------------------------using control statement first time------------------
if int(userinput)==computerchoice:
    print("...............You won...........")
    nestedMearge[row][column]='💵'
    print(f"{list1}\n{list2}\n{list3}")
    sys.exit()
nestedMearge[row][column]='🪛'
print(f"{list1}\n{list2}\n{list3}")
#-----------------------secound choice----------------------------------
userinput=input("enter your 2nd choice : ")
row1=int(userinput[0])-1
column1=int(userinput[1])-1
#----------------------------using control statement secound time------------------
if int(userinput)==computerchoice:
    print("...............You won...........")
    nestedMearge[row1][column1]='💵'
    print(f"{list1}\n{list2}\n{list3}")
    sys.exit()
nestedMearge[row1][column1]='🪛'
print(f"{list1}\n{list2}\n{list3}")
#-----------------------third choice----------------------------------
userinput=input("enter your 3rd choice : ")
row2=int(userinput[0])-1
column2=int(userinput[1])-1
#----------------------------using control statement third time------------------
if int(userinput)==computerchoice:
    print("...............You won...........")
    nestedMearge[row2][column2]='💵'
    print(f"{list1}\n{list2}\n{list3}")
    sys.exit()
nestedMearge[row2][column2]='🪛'
print(f"{list1}\n{list2}\n{list3}")

